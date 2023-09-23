import json
from .serialize import serialize_value, _recurs_for_key


DELETED = "deleted"
ADDED = "added"
NESTED = ".nested"
CHANGED = ".changed"
UNCHANGED = "unchanged"


def json_formatter(data):
    res = {
        "added": [],
        "updated_to": [],
        "removed": []
    }
    old = None
    for line in _recurs_for_key(data, ''):
        value = serialize_value(line['value'])
        status = line["status"]
        key = line['key']
        if old is not None and old["key"] != key and DELETED in old["status"]:
            res.get("removed").append({old["key"]: old["value"]})

        if old is not None and old["key"] == key and DELETED in old["status"]:
            res.get("updated_to").append({key: value})
        elif ADDED in status:
            res.get("added").append({key: value})
        old = line
    return json.dumps(res, indent=4)
