from .plain import plain
from .stylish import stylish
from .json_format import json_formatter


FORMATERS = {
    'stylish': stylish,
    'plain': plain,
    'json': json_formatter,
}


def apply_format(data, format):
    formater = FORMATERS[format]
    return formater(data)
