from .serialize import _recurs_for_key


DELETED = "deleted"
ADDED = "added"
NESTED = "nested"
CHANGED = "changed"
UNCHANGED = "unchanged"


def serialize_value(value):
    if isinstance(value, bool):
        value = str(value).lower()
    elif isinstance(value, str) and value != '[complex value]':
        value = "'{}'".format(value)
    elif value is None:
        value = 'null'
    return value


def plain(data):
    result = []
    old = None
    for line in _recurs_for_key(data, ''):
        value = serialize_value(line['value'])
        status = line["status"]
        key = line['key']
        res_line = None

        if old is not None and old["key"] != key and DELETED in old["status"]:
            res_line = "Property '{}' was removed".format(old["key"])
            result.append(res_line)

        if old is not None and old["key"] == key and DELETED in old["status"]:
            v_ex = serialize_value(old['value'])
            res_line = "Property '{}' was updated. From {} to {}"
            res_line = res_line.format(key, v_ex, value)
            result.append(res_line)

        elif ADDED in status:
            res_line = "Property '{}' was added with value: {}"
            res_line = res_line.format(key, value)
            result.append(res_line)
        old = line
    return '\n'.join(result)
