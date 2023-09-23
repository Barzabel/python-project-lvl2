DELETED = "deleted"
ADDED = "added"
NESTED = ".nested"
CHANGED = ".changed"
UNCHANGED = "unchanged"


def join_value_plain(value):
    if isinstance(value, bool):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    return value


def stylish(data, deap=""):
    res = ["{"]
    for x in data:
        line = ""
        if NESTED in x["status"]:
            new_deap = "    " + deap
            value = stylish(x["value"], new_deap)
        else:
            value = join_value_plain(x["value"])
        if UNCHANGED in x["status"]:
            line = "{}    {}: {}".format(deap, x['key'], value)
        elif ADDED in x["status"]:
            line = "{}  + {}: {}".format(deap, x['key'], value)
        elif DELETED in x["status"]:
            line = "{}  - {}: {}".format(deap, x['key'], value)
        res.append(line)
    end = deap + "}"
    res.append(end)
    return "\n".join(res)
