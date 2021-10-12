def stylish(data, deap=""):
    res = "{"
    for x in data:
        if type(x["value"]) == list:
            new_deap = "    " + deap
            value = stylish(x["value"], new_deap)
        elif type(x["value"]) == bool:
            if x["value"]:
                value = 'true'
            else:
                value = 'false'
        elif x["value"] is None:
            value = 'null'
        else:
            value = x["value"]

        if x["status"] == 0:
            res += "\n{}    {}: {}".format(deap, x['key'], value)
        elif x["status"] == 1:
            res += "\n{}  + {}: {}".format(deap, x['key'], value)
        elif x["status"] == -1:
            res += "\n{}  - {}: {}".format(deap, x['key'], value)
    end = "\n" + deap + "}"
    res += end
    return res
