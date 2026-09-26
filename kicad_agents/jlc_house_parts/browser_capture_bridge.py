"""Local form for saving facts read from live JLC pages in a browser.

This listens only on loopback. It does not fetch supplier pages or decide OOMP
identity; the worker still reviews and promotes one candidate at a time.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from hashlib import sha256
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
import secrets
from urllib.parse import parse_qs


DATA = Path(__file__).resolve().parent
QUEUE = DATA / "queue.json"
STAGING = DATA / "browser_staging"
MAX_POST_BYTES = 65536


def validate_capture(payload: dict, queue: dict[str, dict]) -> dict:
    if not isinstance(payload, dict):
        raise ValueError("Capture must be a JSON object")
    code = payload.get("code", "")
    if not isinstance(code, str) or not re.fullmatch(r"C\d+", code):
        raise ValueError("Code must be a JLC C-number")
    row = queue.get(code)
    if row is None or row.get("retired"):
        raise ValueError("Code is not an active queue item")
    for key, expected in (
        ("official_url", row["jlcpcb_url"]),
        ("manufacturer", row["manufacturer"]),
        ("mpn", row["mpn"]),
        ("package", row["package"]),
    ):
        if payload.get(key) != expected:
            raise ValueError(f"Live {key} differs from the queue; review manually")
    tier = {"Basic": "basic", "Preferred": "preferred_extended",
            "Promotional": "preferred_extended"}.get(payload.get("tier_label"))
    if tier != row["tier"]:
        raise ValueError("Live JLC class differs from the queue")
    if not isinstance(payload.get("description"), str) or not payload["description"].strip():
        raise ValueError("Description is missing")
    if not isinstance(payload.get("specifications"), dict):
        raise ValueError("Specifications must be an object")
    if not isinstance(payload.get("visible_text"), str) or code not in payload["visible_text"]:
        raise ValueError("Visible page text must include the C-number")
    datasheet = payload.get("datasheet_url") or ""
    if datasheet and (not isinstance(datasheet, str) or not datasheet.startswith("https://")
                     or "?" in datasheet):
        raise ValueError("Datasheet URL must be a query-free HTTPS URL")
    capture = dict(payload)
    capture["captured_on"] = datetime.now(timezone.utc).date().isoformat()
    capture["capture_method"] = "interactive_browser_visible_page"
    return capture


def make_handler(queue: dict[str, dict], token: str):
    class Handler(BaseHTTPRequestHandler):
        def _send(self, status: HTTPStatus, body: str, content_type: str = "text/html; charset=utf-8"):
            data = body.encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            if self.path != "/":
                self._send(HTTPStatus.NOT_FOUND, "Not found", "text/plain; charset=utf-8")
                return
            self._send(HTTPStatus.OK, (
                "<!doctype html><meta charset='utf-8'><title>JLC browser capture</title>"
                "<h1>JLC browser capture</h1><form method='post' action='/capture'>"
                f"<input type='hidden' name='token' value='{token}'>"
                "<label for='payload'>Verified visible page facts</label><br>"
                "<textarea id='payload' name='payload' rows='12' cols='100'></textarea><br>"
                "<button type='submit'>Save capture</button></form>"
            ))

        def do_POST(self):
            if self.path != "/capture":
                self._send(HTTPStatus.NOT_FOUND, "Not found", "text/plain; charset=utf-8")
                return
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= MAX_POST_BYTES:
                    raise ValueError("Capture is empty or too large")
                data = parse_qs(self.rfile.read(length).decode("utf-8"), strict_parsing=True)
                if data.get("token", [None])[0] != token:
                    raise ValueError("Invalid local form token")
                payload = json.loads(data["payload"][0])
                capture = validate_capture(payload, queue)
                STAGING.mkdir(parents=True, exist_ok=True)
                target = STAGING / f"{capture['code']}.json"
                if target.exists():
                    raise ValueError("Capture already exists; review it before recapturing")
                encoded = (json.dumps(capture, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
                target.write_bytes(encoded)
                digest = sha256(encoded).hexdigest()
                self._send(HTTPStatus.OK, f"Saved {capture['code']} ({digest})", "text/plain; charset=utf-8")
            except (ValueError, KeyError, UnicodeDecodeError, json.JSONDecodeError) as exc:
                self._send(HTTPStatus.BAD_REQUEST, str(exc), "text/plain; charset=utf-8")

    return Handler


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    queue = {row["code"]: row for row in json.loads(QUEUE.read_text(encoding="utf-8"))}
    server = ThreadingHTTPServer(("127.0.0.1", args.port), make_handler(queue, secrets.token_urlsafe(32)))
    print(f"JLC capture form listening on http://127.0.0.1:{args.port}/", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
