import pytest
import json
import os
from gendiff.gendiff import generate_diff


def get_data_from_file(path):
    root, ext = os.path.splitext(path)
    with open(path, "r") as read_file:
        if ext == ".json":
            return json.dumps(json.load(read_file), indent=4)
        else:
            return read_file.read()


def get_path(name):
    return 'tests/fixtures/{}'.format(name)


@pytest.mark.parametrize(
    argnames='file1_path, file2_path, result_render_path, answer_type',
    argvalues=[
        [
            get_path('file_deap1.json'),
            get_path('file_deap1.json'),
            get_path('empty_json_format.json'),
            'json'
        ],
        [
            get_path('file_deap1.json'),
            get_path('file_deap1.json'),
            get_path('empty_plain_format'),
            'plain'
        ],
        [
            get_path('file_deap1.json'),
            get_path('file_deap2.json'),
            get_path('right_answer_json.json'),
            'json'
        ],
        [
            get_path('file_deap1.json'),
            get_path('file_deap2.json'),
            get_path('right_answer_plain'),
            'plain'
        ],
        [
            get_path('file_deap1.yml'),
            get_path('file_deap2.yml'),
            get_path('right_answer_stylish'),
            'stylish'
        ],
        [
            get_path('1.yaml'),
            get_path('2.yml'),
            get_path('right_answer_yml'),
            'stylish'
        ],
    ],
)
def test_formats(file1_path, file2_path, result_render_path, answer_type):
    result_render = get_data_from_file(result_render_path)
    print(generate_diff(
        file1_path,
        file2_path,
        answer_type
    ))
    assert result_render == generate_diff(
        file1_path,
        file2_path,
        answer_type
    )
