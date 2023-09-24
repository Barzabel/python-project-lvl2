import copy


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


def _recurs_for_key(data, parent):
    for x in data:
        if parent != '':
            new_parent = "{}.{}".format(parent, x["key"])
        else:
            new_parent = x["key"]
        if NESTED in x['status'] and UNCHANGED in x['status']:
            for children in _recurs_for_key(x["value"], new_parent):
                yield children
        elif NESTED in x['status']:
            value = copy.copy(x)
            value["key"] = new_parent
            value["value"] = '[complex value]'
            yield value
        else:
            value = copy.copy(x)
            value["key"] = new_parent
            yield value
