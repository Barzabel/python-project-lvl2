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
            status = ADDED
            value_diff = data2[key]
            res.append(_get_dict(status, key, _rdiff(value_diff, value_diff)))
        elif key not in data2:
            status = DELETED
            value_diff = data1[key]
            res.append(_get_dict(status, key, _rdiff(value_diff, value_diff)))
        else:
            value_diff = data1[key], data2[key]

            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                res.append(_get_dict(
                    NESTED,
                    key,
                    _rdiff(*value_diff)))
            elif data1[key] == data2[key]:
                res.append(_get_dict(
                    UNCHANGED,
                    key,
                    _rdiff(*value_diff)))
            else:
                res.append(_get_dict(
                    CHANGED,
                    key,
                    _rdiff(data1[key], data1[key])))
                res.append(_get_dict(
                    CHANGED,
                    key,
                    _rdiff(data2[key], data2[key])))
    return res


def generate_diff(first_file, second_file, formator="stylish"):
    data1 = get_dict_from_path(first_file)
    data2 = get_dict_from_path(second_file)

    dict_diff = _rdiff(data1, data2)
    return apply_format(dict_diff, formator)
