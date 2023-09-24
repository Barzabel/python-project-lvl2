from .file_parser import get_dict_from_path
from .formater.apply_format import apply_format


DELETED = "deleted"
ADDED = "added"
NESTED = "nested"
CHANGED = "changed"
UNCHANGED = "unchanged"


def _get_dict(status, key, value):
    return {
        "status": status,
        "key": key,
        "value": value
    }


def _is_nested(value):
    return NESTED if isinstance(value, dict) else ""


def is_both_dict(value1, value2):
    return isinstance(value1, dict) and isinstance(value2, dict)


def _rdiff(data1, data2):
    if not isinstance(data1, dict):
        return data1

    keys = set(data1.keys()) | set(data2.keys())
    keys = list(keys)
    keys.sort()
    res = []
    for key in keys:
        status = ''
        value_diff = None
        if key not in data1:
            status += ADDED + _is_nested(data2[key])
            value_diff = data2[key]
            res.append(_get_dict(status, key, _rdiff(value_diff, value_diff)))
        elif key not in data2:
            status += DELETED + _is_nested(data1[key])
            value_diff = data1[key]
            res.append(_get_dict(status, key, _rdiff(value_diff, value_diff)))
        else:
            status = UNCHANGED
            value_diff = data1[key], data2[key]

            both_dict = is_both_dict(data1[key], data2[key])
            if data1[key] == data2[key] or both_dict:
                res.append(_get_dict(
                    status + _is_nested(data1[key]) + _is_nested(data2[key]),
                    key,
                    _rdiff(*value_diff)))

            else:
                res.append(_get_dict(
                    DELETED + _is_nested(data1[key]),
                    key,
                    _rdiff(data1[key], data1[key])))
                res.append(_get_dict(
                    ADDED + _is_nested(data2[key]),
                    key,
                    _rdiff(data2[key], data2[key])))
    return res


def generate_diff(first_file, second_file, formator="stylish"):
    data1 = get_dict_from_path(first_file)
    data2 = get_dict_from_path(second_file)

    dict_diff = _rdiff(data1, data2)
    return apply_format(dict_diff, formator)
