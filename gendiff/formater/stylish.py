DELETED = -1
ADDED = 1
NOTCHANGE = 0


def serialize_value_plain(value):
    if isinstance(value, bool):
        if value:
            value = 'true'
        else:
            value = 'false'
    elif value is None:
        value = 'null'
    return value


def stylish(data, deap=""):
    res = "{"
    for x in data:
        if isinstance(x["value"], list):
            new_deap = "    " + deap
            value = stylish(x["value"], new_deap)
        else:
            value = serialize_value_plain(x["value"])
        if x["status"] == NOTCHANGE:
            res += "\n{}    {}: {}".format(deap, x['key'], value)
        elif x["status"] == ADDED:
            res += "\n{}  + {}: {}".format(deap, x['key'], value)
        elif x["status"] == DELETED:
            res += "\n{}  - {}: {}".format(deap, x['key'], value)
    end = "\n" + deap + "}"
    res += end
    return res
