import json
import yaml
import os


def parse(data, format_file='json') -> dict:
    if format_file == 'json':
        return json.load(data)
    elif format_file == 'yml' or format_file == 'yaml':
        return yaml.safe_load(data)

    raise Exception("invalid file format")


def get_dict_from_path(path):
    root, ext = os.path.splitext(path)
    with open(path, "r") as data:
        return parse(data, ext[1:])
