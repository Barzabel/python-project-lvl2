from .plain import plain
from .stylish import stylish
from .json_format import json_formatter


def apply_format(data, formator):
    if formator == 'stylish':
        return stylish(data)
    elif formator == 'plain':
        return '\n'.join(plain(data))
    elif formator == 'json':
        return json_formatter(data)
    raise Exception("invalid format")
