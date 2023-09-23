from .file_parser import get_dict_from_path
from .formater.reformatting import reformatting


DELETED = "deleted"
ADDED = "added"
NESTED = ".nested"
CHANGED = ".changed"
UNCHANGED = "unchanged"


def _get_dict(status, key, value):
    return {
        "status": status,
        "key": key,
        "value": value
    }


def _rdiff(data1, data2):
    if type(data2) is not dict or type(data1) is not dict:
        return data1

    keys = set(data1.keys()) | set(data2.keys())
    keys = list(keys)
    keys.sort()
    res = []
    for key in keys:
        status = ''
        value_diff = None
        if key not in data1:
            status += ADDED
            if type(data2[key]) is dict or type(data2[key]) is list:
                status += NESTED
            value_diff = data2[key]
        elif key not in data2:
            status += DELETED
            if type(data1[key]) is dict or type(data1[key]) is list:
                status += NESTED

            value_diff = data1[key]
        else:
            status = UNCHANGED
            value_diff = data1[key], data2[key]
        if status == UNCHANGED:
            if data1[key] == data2[key]:
                res.append(_get_dict(
                    status + NESTED if type(data1[key]) is dict else status,
                    key,
                    _rdiff(*value_diff)))
            elif type(data1[key]) is dict and type(data2[key]) is dict:
                res.append(_get_dict(status + NESTED, key, _rdiff(*value_diff)))
            else:
                res.append(_get_dict(
                    DELETED + NESTED if type(data1[key]) is dict else DELETED,
                    key,
                    _rdiff(data1[key], data1[key])))
                res.append(_get_dict(
                    ADDED + NESTED if type(data2[key]) is dict else ADDED,
                    key,
                    _rdiff(data2[key], data2[key])))
        else:
            if type(value_diff) is dict:
                res.append(
                    _get_dict(status, key, _rdiff(value_diff, value_diff)))
            else:
                res.append(_get_dict(status, key, value_diff))
    return res


def generate_diff(path1, path2, formator="stylish"):
    data1 = get_dict_from_path(path1)
    data2 = get_dict_from_path(path2)

    dict_diff = _rdiff(data1, data2)
    return reformatting(dict_diff, formator)
