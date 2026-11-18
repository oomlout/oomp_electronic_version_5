"""Small dependency-free reader for KiCad's modern S-expression files."""

from pathlib import Path


class SExpressionError(ValueError):
    """Raised when a KiCad S-expression cannot be parsed."""


def _tokens(text):
    index = 0
    length = len(text)

    while index < length:
        character = text[index]

        if character.isspace():
            index += 1
            continue

        if character == ";":
            while index < length and text[index] not in "\r\n":
                index += 1
            continue

        if character in "()":
            yield character
            index += 1
            continue

        if character == '"':
            index += 1
            value = []
            while index < length:
                character = text[index]
                if character == '"':
                    index += 1
                    break
                if character == "\\":
                    index += 1
                    if index >= length:
                        raise SExpressionError("Unterminated escape in quoted string")
                    escaped = text[index]
                    replacements = {"n": "\n", "r": "\r", "t": "\t"}
                    value.append(replacements.get(escaped, escaped))
                    index += 1
                    continue
                value.append(character)
                index += 1
            else:
                raise SExpressionError("Unterminated quoted string")
            yield "".join(value)
            continue

        start = index
        while index < length and not text[index].isspace() and text[index] not in "()":
            index += 1
        yield text[start:index]


def loads(text):
    """Parse one S-expression and return nested Python lists and string atoms."""
    root = None
    stack = []

    for token in _tokens(text):
        if token == "(":
            node = []
            if stack:
                stack[-1].append(node)
            elif root is not None:
                raise SExpressionError("More than one top-level expression")
            else:
                root = node
            stack.append(node)
        elif token == ")":
            if not stack:
                raise SExpressionError("Unexpected closing parenthesis")
            stack.pop()
        else:
            if not stack:
                raise SExpressionError("Atom outside an expression")
            stack[-1].append(token)

    if stack:
        raise SExpressionError("Unclosed expression")
    if root is None:
        raise SExpressionError("Empty S-expression")
    return root


def load(path):
    path = Path(path)
    return loads(path.read_text(encoding="utf-8"))


def tag(node):
    if isinstance(node, list) and node and isinstance(node[0], str):
        return node[0]
    return ""


def children(node, child_tag):
    return [item for item in node[1:] if isinstance(item, list) and tag(item) == child_tag]


def child(node, child_tag):
    for item in node[1:]:
        if isinstance(item, list) and tag(item) == child_tag:
            return item
    return None


def value(node, child_tag, default=""):
    item = child(node, child_tag)
    if item is None or len(item) < 2:
        return default
    return item[1]


def values(node, child_tag):
    item = child(node, child_tag)
    if item is None:
        return []
    return [item_value for item_value in item[1:] if isinstance(item_value, str)]


def as_float(raw_value, default=0.0):
    try:
        return float(raw_value)
    except (TypeError, ValueError):
        return default


def as_int(raw_value, default=0):
    try:
        return int(raw_value)
    except (TypeError, ValueError):
        return default


def as_bool(raw_value, default=False):
    if raw_value == "yes":
        return True
    if raw_value == "no":
        return False
    return default

