import json
import yaml
import os


def parse(data, format_file='json') -> dict:
    if format_file == 'json':
        dict_from_data = json.load(data)
    elif format_file == 'yml' or format_file == 'yaml':
        dict_from_data = yaml.safe_load(data)
    else:
        raise Exception("invalid file format")
    return dict_from_data


def get_dict_from_path(path):
    root, ext = os.path.splitext(path)
    with open(path, "r") as data:
        return parse(data, ext[1:])
