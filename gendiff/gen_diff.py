import json
import yaml
from pathlib import Path


def get_path(path):
    cwd_dir = Path.cwd()
    res_path = Path(cwd_dir, path)
    return res_path


def get_dict_from_path(path1, path2):
    format_file = path1.split('.')[-1]
    if format_file == 'json':
        with open(get_path(path1), "r") as read_file:
            data1 = json.load(read_file)
        with open(get_path(path2), "r") as read_file:
            data2 = json.load(read_file)
        return data1, data2
    elif format_file == 'yml' or format_file =='yaml':
        with open(get_path(path1), "r") as read_file:
            data1 = yaml.safe_load(read_file)
        with open(get_path(path2), "r") as read_file:
            data2 = yaml.safe_load(read_file)
        return data1, data2




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
