DELETED = "deleted"
ADDED = "added"
NESTED = "nested"
CHANGED = "changed"
UNCHANGED = "unchanged"


def join_value_stylish(value):
    if isinstance(value, bool):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    return value


def get_line_str(status, key, value, deap):
    line = ""
    if UNCHANGED in status:
        line = "{}    {}: {}".format(deap, key, value)
    elif ADDED in status:
        line = "{}  + {}: {}".format(deap, key, value)
    elif DELETED in status:
        line = "{}  - {}: {}".format(deap, key, value)
    return line


def stylish(data, deap=""):
    res = ["{"]
    for x in data:
        if NESTED in x["status"]:
            new_deap = "    " + deap
            value = stylish(x["value"], new_deap)
        else:
            value = join_value_stylish(x["value"])
        line = get_line_str(x["status"], x['key'], value, deap)
        res.append(line)
    end = deap + "}"
    res.append(end)
    return "\n".join(res)
