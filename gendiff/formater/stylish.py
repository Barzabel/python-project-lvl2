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


def get_next_node(status, key, value, deap):
    line = ""
    new_deap = "    " + deap
    if UNCHANGED == status or NESTED == status:
        line = "{}    {}: {}"
    elif ADDED == status:
        line = "{}  + {}: {}"
    elif DELETED == status:
        line = "{}  - {}: {}"
    return line.format(deap, key, stylish(value, new_deap))


def stylish(data, deap=""):
    if isinstance(data, str | int):
        return data
    res = ["{"]
    first_cahnged = True
    for x in data:
        value = join_value_stylish(x["value"])
        if x["status"] == CHANGED:
            if first_cahnged:
                line = get_next_node(DELETED, x['key'], value, deap)
                first_cahnged = False
            else:
                line = get_next_node(ADDED, x['key'], value, deap)
                first_cahnged = True
        else:
            line = get_next_node(x["status"], x['key'], value, deap)
        res.append(line)

    end = deap + "}"
    res.append(end)
    return "\n".join(res)
