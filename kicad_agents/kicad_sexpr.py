"""Quoted-atom-preserving KiCad reader/writer for generated library/design copies.

Unlike the extraction reader, this distinguishes a quoted '(' from syntax and
never guesses whether a string such as a pin number should be quoted.
"""

import json
import re
from decimal import Decimal, InvalidOperation


class Atom(str):
    def __new__(cls, value, quoted=False):
        result = super().__new__(cls, value)
        result.quoted = quoted
        return result


def q(value):
    return Atom(str(value), True)


def parse(text):
    tokens = re.finditer(r'\s+|;[^\n]*|"(?:\\.|[^"\\])*"|[()]|[^\s()";]+', text)
    stack = []
    root = None
    end = 0
    for match in tokens:
        if match.start() != end:
            raise ValueError(f"Invalid KiCad syntax at character {end}")
        end = match.end()
        token = match.group()
        if token.isspace() or token.startswith(';'):
            continue
        if token == '(':
            node = []
            if stack:
                stack[-1].append(node)
            elif root is not None:
                raise ValueError("Multiple KiCad roots")
            else:
                root = node
            stack.append(node)
        elif token == ')':
            if not stack:
                raise ValueError("Unbalanced KiCad parentheses")
            stack.pop()
        else:
            if not stack:
                raise ValueError("KiCad atom outside root")
            if token.startswith('"'):
                # KiCad uses backslash escapes; keep unfamiliar escapes intact.
                value = re.sub(r'\\([\\"nrt])', lambda m: {'n': '\n', 'r': '\r', 't': '\t'}.get(m[1], m[1]), token[1:-1])
                stack[-1].append(q(value))
            else:
                stack[-1].append(Atom(token))
    if stack or root is None or end != len(text):
        raise ValueError("Incomplete KiCad expression")
    return root


def dumps(node):
    if isinstance(node, list):
        return '(' + ' '.join(dumps(item) for item in node) + ')'
    if getattr(node, 'quoted', False):
        return json.dumps(str(node), ensure_ascii=False)
    return str(node)


def document(root):
    """Keep top-level items on separate lines; preserve all atom quoting."""
    lines = []
    for item in root:
        lines.append(dumps(item))
    return '(' + '\n  '.join(lines) + '\n)\n'


def tag(node):
    return str(node[0]) if isinstance(node, list) and node else ''


def children(node, name):
    return [item for item in node if tag(item) == name]


def child(node, name):
    return next(iter(children(node, name)), None)


def value(node, name, default=''):
    item = child(node, name)
    return str(item[1]) if item and len(item) > 1 else default


def property_value(node, name):
    for item in children(node, 'property'):
        if item[1] == name:
            return str(item[2])
    return ''


def canonical(node):
    """Ignore harmless list ordering, except for ordered geometry point lists."""
    if not isinstance(node, list):
        if not getattr(node, 'quoted', False):
            try:
                return ('number', str(Decimal(str(node)).normalize()))
            except InvalidOperation:
                pass
        return ('atom', str(node))
    atoms = []
    nested = []
    for item in node:
        if isinstance(item, list):
            nested.append(canonical(item))
        else:
            atoms.append(canonical(item))
    if tag(node) not in ['pts', 'polygon', 'coordinates']:
        nested.sort(key=repr)
    return ('node', tuple(atoms), tuple(nested))
