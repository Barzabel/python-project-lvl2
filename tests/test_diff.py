import pytest
import json
from gendiff.gendiff import generate_diff


@pytest.fixture
def result_json_empty():
    with open('tests/fixtures/empty_json_format.json', "r") as read_file:
        return '{0}\n'.format(json.dumps(json.load(read_file), indent=4))


@pytest.fixture
def result_within_json():
    with open('tests/fixtures/right_answer_json.json', "r") as read_file:
        return '{0}\n'.format(json.dumps(json.load(read_file), indent=4))


@pytest.fixture
def result_within_plain():
    with open('tests/fixtures/right_answer_plain', "r") as read_file:
        return read_file.read()


@pytest.fixture
def result_within_stylish():
    with open('tests/fixtures/right_answer_stylish', "r") as read_file:
        return read_file.read()


@pytest.fixture
def result_stylish():
    return '{\n    age: 35\n  + cat: true\n    children: true\n    firstName: Jane\n    hobbies: false\n  - lalala: 1\n  - lastName: Doe\n  + lastName: andr\n}'


def test_empty_result(result_json_empty):
    empty_json = generate_diff('tests/fixtures/file_deap1.json', 'tests/fixtures/file_deap1.json', "json")
    assert empty_json == result_json_empty
    assert generate_diff('tests/fixtures/file_deap1.json', 'tests/fixtures/file_deap1.json', "plain") == ''


def test_json_within_json(result_within_json, result_within_plain, result_within_stylish):
    assert generate_diff('tests/fixtures/file_deap1.json', 'tests/fixtures/file_deap2.json', "json") == result_within_json
    assert generate_diff('tests/fixtures/file_deap1.json', 'tests/fixtures/file_deap2.json', "plain") == result_within_plain
    assert generate_diff('tests/fixtures/file_deap1.yml', 'tests/fixtures/file_deap2.yml') == result_within_stylish


def test_yaml(result_stylish):
    assert generate_diff('tests/fixtures/1.yaml', 'tests/fixtures/2.yml') == result_stylish
