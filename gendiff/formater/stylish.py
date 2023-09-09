DELETED = -1
ADDED = 1
NOTCHANGE = 0


def join_value_plain(value):
    if isinstance(value, bool):
        if value:
            value = 'true'
        else:
            value = 'false'
    elif value is None:
        value = 'null'
    return value


def stylish(data, deap=""):
    res = ["{"]
    for x in data:
        line = ""
        if isinstance(x["value"], list):
            new_deap = "    " + deap
            value = stylish(x["value"], new_deap)
        else:
            value = join_value_plain(x["value"])
        if x["status"] == NOTCHANGE:
            line = "{}    {}: {}".format(deap, x['key'], value)
        elif x["status"] == ADDED:
            line = "{}  + {}: {}".format(deap, x['key'], value)
        elif x["status"] == DELETED:
            line = "{}  - {}: {}".format(deap, x['key'], value)
        res.append(line)
    end = deap + "}"
    res.append(end)
    return "\n".join(res)
