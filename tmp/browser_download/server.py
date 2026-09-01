from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class RedirectHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/datasheet.pdf":
            self.send_response(302)
            self.send_header(
                "Location",
                "https://product.tdk.com/en/system/files/dam/doc/product/emc/emc/beads/catalog/beads_commercial_signal_mmz2012_en.pdf",
            )
            self.end_headers()
            return
        return super().do_GET()


server = ThreadingHTTPServer(("127.0.0.1", 8765), RedirectHandler)
server.serve_forever()
