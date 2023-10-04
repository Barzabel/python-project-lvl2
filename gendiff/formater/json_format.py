import json


DELETED = "deleted"
ADDED = "added"
NESTED = "nested"
CHANGED = "changed"
UNCHANGED = "unchanged"


def serialize_value(value):
    if isinstance(value, list):
        return '[complex value]'
    if isinstance(value, bool):
        value = str(value).lower()
    elif isinstance(value, str):
        value = "'{}'".format(value)
    elif value is None:
        value = 'null'
    return value


def get_parent(parent, key):
    if parent != '':
        return "{}.{}".format(parent, key)
    else:
        return key


def json_formatter(data): # noqa C901
    res = {
        "added": [],
        "updated_to": [],
        "removed": []
    }

    def wolk(data, parent=''):
        first_cahnged = True
        for x in data:
            new_parent = get_parent(parent, x["key"])
            if x['status'] == NESTED:
                wolk(x["value"], new_parent)
            value = serialize_value(x["value"])
            if x['status'] == CHANGED:
                if first_cahnged:
                    first_cahnged = False
                else:
                    res.get("updated_to").append({new_parent: value})
                    first_cahnged = True
            elif x['status'] == DELETED:
                res.get("removed").append({new_parent: value})
            elif x['status'] == ADDED:
                res.get("added").append({new_parent: value})
    wolk(data)
    return json.dumps(res, indent=4)
