from .file_parser import get_dict_from_path
from .formater.plain import plain
from .formater.stylish import stylish
from .formater.json_format import json_formatter


def _get_dict(status, key, value):
    return {
        "status": status,
        "key": key,
        "value": value
    }


def _rdiff(data1, data2):
    if type(data2) != dict or type(data1) != dict:
        return data1

    keys = set(data1.keys()) | set(data2.keys())
    keys = list(keys)
    keys.sort()
    res = []
    status = 0

    for key in keys:
        value_diff = None
        if key not in data1:
            status = 1
            value_diff = data2[key]
        elif key not in data2:
            status = -1
            value_diff = data1[key]
        else:
            status = 0
            value_diff = data1[key], data2[key]

        if status == 0:
            if data1[key] == data2[key]:
                res.append(_get_dict(status, key, _rdiff(*value_diff)))
            elif type(data1[key]) == dict and type(data2[key]) == dict:
                res.append(_get_dict(status, key, _rdiff(*value_diff)))
            else:
                res.append(_get_dict(-1, key, _rdiff(data1[key], data1[key])))
                res.append(_get_dict(1, key, _rdiff(data2[key], data2[key])))
        else:
            if type(value_diff) == dict:
                res.append(
                    _get_dict(status, key, _rdiff(value_diff, value_diff)))
            else:
                res.append(_get_dict(status, key, value_diff))
    return res


def generate_diff(path1, path2, formator="stylish"):
    data1, data2 = get_dict_from_path(path1, path2)
    if formator == 'stylish':
        return stylish(_rdiff(data1, data2))
    elif formator == 'plain':
        return plain(_rdiff(data1, data2))
    elif formator == 'json':
        return json_formatter(_rdiff(data1, data2))
