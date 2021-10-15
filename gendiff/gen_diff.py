from .file_parser import get_dict_from_path
from .formater.plain import plain
from .formater.stylish import stylish

def _rec_diff2(data1, data2):
    keys = set(data1.keys()) | set(data2.keys())
    keys = list(keys)
    keys.sort()
    res = []
    for x in keys:
        if x in data1 and x in data2:
            if data1[x] == data2[x]:
                if type(data1[x]) == dict:
                    res.append({
                        "status": 0,
                        "key": x,
                        "value": _rec_diff2(data1[x], data2[x])
                        })
                else:
                    res.append({
                        "status": 0,
                        "key": x,
                        "value": data1[x]
                        })
            else:
                if type(data1[x]) == dict and type(data2[x]) != dict:
                    res.append({
                        "status": -1,
                        "key": x,
                        "value": _rec_diff2(data1[x], data1[x])
                        })
                    res.append({
                        "status": +1,
                        "key": x,
                        "value": data2[x]
                        })

                elif type(data1[x]) != dict and type(data2[x]) == dict:
                    res.append({
                        "status": -1,
                        "key": x,
                        "value": data1[x]
                        })
                    res.append({
                        "status": +1,
                        "key": x,
                        "value": _rec_diff2(data2[x], data2[x])
                        })
                elif type(data1[x]) == dict and type(data2[x]) == dict:
                    res.append({
                        "status": 0,
                        "key": x,
                        "value": _rec_diff2(data1[x], data2[x])
                        })
                else:
                    res.append({
                        "status": -1,
                        "key": x,
                        "value": data1[x]
                        })
                    res.append({
                        "status": 1,
                        "key": x,
                        "value": data2[x]
                        })
        elif x in data1 and x not in data2:
            if type(data1[x]) == dict:
                res.append({
                    "status": -1,
                    "key": x,
                    "value": _rec_diff2(data1[x], data1[x])
                    })
            else:
                res.append({
                    "status": -1,
                    "key": x,
                    "value": data1[x]
                    })
        elif x not in data1 and x in data2:
            if type(data2[x]) == dict:
                res.append({
                    "status": +1,
                    "key": x,
                    "value": _rec_diff2(data2[x], data2[x])
                    })
            else:
                res.append({
                    "status": 1,
                    "key": x,
                    "value": data2[x]
                    })
    return res


def generate_diff(path1, path2, formator="stylish"):
    data1, data2 = get_dict_from_path(path1, path2)
    if formator == 'stylish':
        return stylish(_rec_diff2(data1, data2))
    elif formator == 'plain':
        return plain(_rec_diff2(data1, data2))

    
