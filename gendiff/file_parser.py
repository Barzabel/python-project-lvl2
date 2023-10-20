import json
import yaml
import os


PARSERS = {
    '.yaml': lambda x: yaml.safe_load(x),
    '.yml': lambda x: yaml.safe_load(x),
    '.json': lambda x: json.load(x),
}


def get_dict_from_path(path):
    root, ext = os.path.splitext(path)
    parser = PARSERS[ext]
    with open(path, "r") as data:
        return parser(data)
