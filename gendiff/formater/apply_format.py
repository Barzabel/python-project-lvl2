from .plain import plain
from .stylish import stylish
from .json_format import json_formatter


def apply_format(data, format):
    if format == 'stylish':
        return stylish(data)
    elif format == 'plain':
        return plain(data)
    elif format == 'json':
        return json_formatter(data)
    raise Exception("invalid format")
