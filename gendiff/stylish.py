import copy


def serialize_value_json(value):
    if type(value) == bool:
        if value:
            value = 'true'
        else:
            value = 'false'
    elif value is None:
        value = 'null'
    return value


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


def stylish(data, deap=""):
    res = "{"
    for x in data:
        if type(x["value"]) == list:
            new_deap = "    " + deap
            value = stylish(x["value"], new_deap)
        else:
            value = serialize_value_json(x["value"])
        if x["status"] == 0:
            res += "\n{}    {}: {}".format(deap, x['key'], value)
        elif x["status"] == 1:
            res += "\n{}  + {}: {}".format(deap, x['key'], value)
        elif x["status"] == -1:
            res += "\n{}  - {}: {}".format(deap, x['key'], value)
    end = "\n" + deap + "}"
    res += end
    return res


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
    res = ""
    for x in range(len(new_data)):
        value = serialize_value_plain(new_data[x]['value'])
        status = new_data[x]["status"]
        if new_data[x]["status"] == 1:
            key = new_data[x]['key']
            line = "\nProperty '{}' was added with value: {}"
            res += line.format(key, value)
        elif status == -1 and new_data[x]['key'] == new_data[x + 1]['key']:
            v_next = serialize_value_plain(new_data[x + 1]['value'])
            key = new_data[x]['key']
            line = "\nProperty '{}' was updated. From {} to {}"
            res += line.format(key, value, v_next)
            new_data[x + 1]['status'] = None
        elif new_data[x]["status"] == -1:
            res += "\nProperty '{}' was removed".format(new_data[x]['key'])
    return res
