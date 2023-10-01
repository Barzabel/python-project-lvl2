DELETED = "deleted"
ADDED = "added"
NESTED = "nested"
CHANGED = "changed"
UNCHANGED = "unchanged"


def serialize_value(value):
    if isinstance(value, list):
        return '[complex value]'
    if isinstance(value, bool):
        value = str(value).lower()
    elif isinstance(value, str):
        value = "'{}'".format(value)
    elif value is None:
        value = 'null'
    return value


def get_path(path, key):
    if path != '':
        return "{}.{}".format(path, key)
    else:
        return key


def get_old(status, key, value):
    if CHANGED in status:
        old = value
        old['key'] = key
    else:
        old = None
    return old


def plain(data, path=""):
    result = []
    old = None
    for var in data:
        new_path = get_path(path, var["key"])
        status = var["status"]
        if NESTED in status and UNCHANGED in status:
            result.extend(plain(var["value"], new_path))
        value = serialize_value(var['value'])
        res_line = None

        if old and old["key"] == new_path and DELETED in old["status"]:
            v_ex = serialize_value(old['value'])
            res_line = "Property '{}' was updated. From {} to {}"
            res_line = res_line.format(new_path, v_ex, value)
            result.append(res_line)
        elif ADDED in status:
            res_line = "Property '{}' was added with value: {}"
            res_line = res_line.format(new_path, value)
            result.append(res_line)
        elif DELETED in status and CHANGED not in status:
            res_line = "Property '{}' was removed".format(new_path)
            result.append(res_line)
        old = get_old(status, new_path, var)
    return result
