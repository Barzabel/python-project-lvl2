from .serialize import serialize_value_plain, _recurs_for_key


def plain(data):
    new_data = _recurs_for_key(data, '')
    result = []
    for x in range(len(new_data)):
        value = serialize_value_plain(new_data[x]['value'])
        status = new_data[x]["status"]
        key = new_data[x]['key']
        is_end = x < len(new_data) - 1
        line = None
        if new_data[x]["status"] == 1:
            line = "Property '{}' was added with value: {}"
            line = line.format(key, value)
        elif status == -1 and is_end and key == new_data[x + 1]['key']:
            v_next = serialize_value_plain(new_data[x + 1]['value'])
            line = "Property '{}' was updated. From {} to {}"
            line = line.format(key, value, v_next)
            new_data[x + 1]['status'] = None
        elif new_data[x]["status"] == -1:
            line = "Property '{}' was removed".format(new_data[x]['key'])

        if line:
            result.append(line)
    return '\n'.join(result)
