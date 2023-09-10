import json
from .serialize import serialize_value_plain, _recurs_for_key


DELETED = -1
ADDED = 1


def json_formatter(data):
    new_data = _recurs_for_key(data, '')
    res = {
        "added": [],
        "updated_to": [],
        "removed": []
    }

    for x in range(len(new_data)):
        value = serialize_value_plain(new_data[x]['value'])
        status = new_data[x]["status"]
        key = new_data[x]['key']
        is_end = x < len(new_data) - 1
        if new_data[x]["status"] == ADDED:
            key = new_data[x]['key']
            res.get("added").append({key: value})
        elif status == DELETED and is_end and key == new_data[x + 1]['key']:
            v_next = serialize_value_plain(new_data[x + 1]['value'])
            res.get("updated_to").append({key: v_next})
            new_data[x + 1]['status'] = None
        elif new_data[x]["status"] == DELETED:
            res.get("removed").append({key: value})
    return json.dumps(res, indent=4) 
