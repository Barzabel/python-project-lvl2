from .plain import plain
from .stylish import stylish
from .json_format import json_formatter


def reformatting(data, formator):
    if formator == 'stylish':
        return stylish(data)
    elif formator == 'plain':
        return plain(data)
    elif formator == 'json':
        return json_formatter(data)
