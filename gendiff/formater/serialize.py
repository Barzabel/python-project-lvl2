import copy


NOTCHANGE = 0


def serialize_value_plain(value):
    if isinstance(value, bool):
        if value:
            value = 'true'
        else:
            value = 'false'
    elif isinstance(value, str) and value != '[complex value]':
        value = "'{}'".format(value)
    elif value is None:
        value = 'null'
    return value


def _recurs_for_key(data, parent):
    new_data = []
    for x in data:
        if isinstance(x["value"], list) and x['status'] == NOTCHANGE:
            if parent != '':
                new_parent = "{}.{}".format(parent, x["key"])
            else:
                new_parent = x["key"]
            for y in _recurs_for_key(x["value"], new_parent):
                new_data.append(y)
        elif isinstance(x["value"], list) and (x['status'] != NOTCHANGE):
            value = copy.copy(x)
            if parent != "":
                value["key"] = "{}.{}".format(parent, x["key"])
            value["value"] = '[complex value]'
            new_data.append(value)
        else:
            value = copy.copy(x)
            if parent != "":
                value["key"] = "{}.{}".format(parent, x["key"])
            new_data.append(value)
    return new_data
