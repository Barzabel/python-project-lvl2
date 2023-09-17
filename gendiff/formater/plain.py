from .serialize import serialize_value, _recurs_for_key


DELETED = -1
ADDED = 1
NOTCHANGE = 0


def plain(data):
    result = []
    old = None
    for line in _recurs_for_key(data, ''):
        value = serialize_value(line['value'])
        status = line["status"]
        key = line['key']
        res_line = None

        if old is not None and old["key"] != key and old["status"] == DELETED:
            res_line = "Property '{}' was removed".format(old["key"])
            result.append(res_line)

        if old is not None and old["key"] == key and old["status"] == DELETED:
            v_ex = serialize_value(old['value'])
            res_line = "Property '{}' was updated. From {} to {}"
            res_line = res_line.format(key, v_ex, value)
            result.append(res_line)

        elif status == ADDED:
            res_line = "Property '{}' was added with value: {}"
            res_line = res_line.format(key, value)
            result.append(res_line)
        old = line
    return '\n'.join(result)
