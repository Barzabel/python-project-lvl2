import pytest
import json
import os
from gendiff.gendiff import generate_diff


def get_data_from_file(path):
    root, ext = os.path.splitext(path)
    with open(path, "r") as read_file:
        if ext == ".json":
            return '{0}\n'.format(json.dumps(json.load(read_file), indent=4))
        else:
            return read_file.read()


@pytest.mark.parametrize(
    argnames='prepared_files',
    argvalues=[
        [
            'tests/fixtures/file_deap1.json',
            'tests/fixtures/file_deap1.json',
            'tests/fixtures/empty_json_format.json',
            'json'
        ],
        [
            'tests/fixtures/file_deap1.json',
            'tests/fixtures/file_deap1.json',
            'tests/fixtures/empty_plain_format',
            'plain'
        ],
        [
            'tests/fixtures/file_deap1.json',
            'tests/fixtures/file_deap2.json',
            'tests/fixtures/right_answer_json.json',
            'json'
        ],
        [
            'tests/fixtures/file_deap1.json',
            'tests/fixtures/file_deap2.json',
            'tests/fixtures/right_answer_plain',
            'plain'
        ],
        [
            'tests/fixtures/file_deap1.yml',
            'tests/fixtures/file_deap2.yml',
            'tests/fixtures/right_answer_stylish',
            'stylish'
        ],
    ],
)
def test_formats(prepared_files):
    file1_path, file2_path, result_render_path, answer_type = prepared_files
    result_render = get_data_from_file(result_render_path)
    assert result_render == generate_diff(
        file1_path,
        file2_path,
        answer_type
    )


@pytest.mark.parametrize(
    argnames='test_input,expected',
    argvalues=[(('tests/fixtures/1.yaml', 'tests/fixtures/2.yml'),
                'tests/fixtures/right_answer_yml'), ],
)
def test_yaml(test_input, expected):
    assert generate_diff(*test_input) == get_data_from_file(expected)
