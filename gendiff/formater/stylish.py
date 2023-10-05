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


def stylish(data, deap=""):
    if isinstance(data, str | int):
        return data
    res = ["{"]
    for x in data:
        status = x["status"]
        key = x['key']
        value = join_value_stylish(x["value"])
        new_deap = "    " + deap
        if status == UNCHANGED or status == NESTED:
            res.append("{}    {}: {}".format(
                deap,
                key,
                stylish(value, new_deap)))
        elif status == CHANGED:
            old_value = join_value_stylish(x["old_value"])
            res.append("{}  - {}: {}".format(
                deap,
                key,
                stylish(old_value, new_deap)))
            res.append("{}  + {}: {}".format(
                deap,
                key,
                stylish(value, new_deap)))
        elif ADDED == status:
            res.append("{}  + {}: {}".format(
                deap,
                key,
                stylish(value, new_deap)))
        elif DELETED == status:
            res.append("{}  - {}: {}".format(
                deap,
                key,
                stylish(value, new_deap)))
    end = deap + "}"
    res.append(end)
    return "\n".join(res)
