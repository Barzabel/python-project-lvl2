import copy


def serialize_value_plain(value):
    if type(value) == bool:
        if value:
            value = 'true'
        else:
            value = 'false'
    elif type(value) == str and value != '[complex value]':
        value = "'{}'".format(value)
    elif value is None:
        value = 'null'
    return value


def _recurs_for_key(data, parent):
    new_data = []
    for x in data:
        if type(x["value"]) == list and x['status'] == 0:
            if parent != '':
                new_parent = "{}.{}".format(parent, x["key"])
            else:
                new_parent = x["key"]
            for y in _recurs_for_key(x["value"], new_parent):
                new_data.append(y)
        elif type(x["value"]) == list and (x['status'] != 0):
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


def plain(data):
    new_data = _recurs_for_key(data, '')
    result = []
    for x in range(len(new_data)):
        value = serialize_value_plain(new_data[x]['value'])
        status = new_data[x]["status"]
        key = new_data[x]['key']
        is_end = x < len(new_data) - 1
        line = None
        if new_data[x]["status"] == 1:
            line = "Property '{}' was added with value: {}"
            line = line.format(key, value)
        elif status == -1 and is_end and key == new_data[x + 1]['key']:
            v_next = serialize_value_plain(new_data[x + 1]['value'])
            line = "Property '{}' was updated. From {} to {}"
            line = line.format(key, value, v_next)
            new_data[x + 1]['status'] = None
        elif new_data[x]["status"] == -1:
            line = "Property '{}' was removed".format(new_data[x]['key'])

        if line:
            result.append(line)
    return '\n'.join(result)
