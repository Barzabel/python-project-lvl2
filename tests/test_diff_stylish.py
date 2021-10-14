import pytest
from gendiff.gen_diff import generate_diff


@pytest.fixture
def result():
    return '{\n    age: 35\n  + cat: true\n    children: true\n    firstName: Jane\n    hobbies: false\n  - lalala: 1\n  - lastName: Doe\n  + lastName: andr\n}'


@pytest.fixture
def result_for_deap():
    with open('tests/fixtures/right_answer_stylish', "r") as read_file:
        return read_file.read()


def test_json(result):
    assert generate_diff('tests/fixtures/1.json', 'tests/fixtures/2.json') == result


def test_yaml(result):
    assert generate_diff('tests/fixtures/1.yaml', 'tests/fixtures/2.yml') == result


def test_json_deap(result_for_deap):
    assert generate_diff('tests/fixtures/file_deap1.json', 'tests/fixtures/file_deap2.json') == result_for_deap


def test_yaml_deap(result_for_deap):
    assert generate_diff('tests/fixtures/file_deap1.yml', 'tests/fixtures/file_deap2.yml') == result_for_deap