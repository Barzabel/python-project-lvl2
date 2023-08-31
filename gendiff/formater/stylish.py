def serialize_value_json(value):
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
