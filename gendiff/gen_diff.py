from .file_parser import get_dict_from_path


def generate_diff(path1, path2):
    data1, data2 = get_dict_from_path(path1, path2)
    keys = set(data1.keys()) | set(data2.keys())
    keys = list(keys)
    keys.sort()
    res = "{"
    for x in keys:
        if x in data1 and x in data2:
            if data1[x] == data2[x]:
                res += "\n    {}: {}".format(x, data1[x])
            else:
                res += "\n  - {}: {}".format(x, data1[x])
                res += "\n  + {}: {}".format(x, data2[x])
        elif x in data1 and x not in data2:
            res += "\n  - {}: {}".format(x, data1[x])
        elif x not in data1 and x in data2:
            res += "\n  + {}: {}".format(x, data2[x])
    res += "\n}"
    return res
