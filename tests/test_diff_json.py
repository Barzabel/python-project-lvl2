import pytest
import json
from gendiff.gendiff import generate_diff


@pytest.fixture
def result_for_deap():
    with open('tests/fixtures/right_answer_json.json', "r") as read_file:
        return json.load(read_file)


@pytest.fixture
def empaty_json_format():
    with open('tests/fixtures/empaty_json_format.json', "r") as read_file:
        return json.load(read_file)


def test_json(empaty_json_format):
    res = generate_diff('tests/fixtures/file_deap1.json', 'tests/fixtures/file_deap1.json', "json")
    assert res == '{0}\n'.format(json.dumps(empaty_json_format, indent=4))


def test_json_deap(result_for_deap):
    res = generate_diff('tests/fixtures/file_deap1.json', 'tests/fixtures/file_deap2.json', "json")
    assert res == '{0}\n'.format(json.dumps(result_for_deap, indent=4))
