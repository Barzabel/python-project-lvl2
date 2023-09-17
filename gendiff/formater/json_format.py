import json
from .serialize import serialize_value, _recurs_for_key

DELETED = -1
ADDED = 1
NOTCHANGE = 0


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
        if old is not None and old["key"] != key and old["status"] == DELETED:
            res.get("removed").append({old["key"]: old["value"]})

        if old is not None and old["key"] == key and old["status"] == DELETED:
            res.get("updated_to").append({key: value})
        elif status == ADDED:
            res.get("added").append({key: value})
        old = line

    return json.dumps(res, indent=4)
