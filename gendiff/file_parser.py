import json
import yaml


def parser_data(data, format_file='json') -> dict:
    if format_file == 'json':
        dict_from_data = json.load(data)
    elif format_file == 'yml' or format_file == 'yaml':
        dict_from_data = yaml.safe_load(data)
    return dict_from_data


def get_dict_from_path(path1):
    format_file = path1.split('.')[-1]
    with open(path1, "r") as data:
        return parser_data(data, format_file)
