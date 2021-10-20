import pytest
import json
from gendiff.generate_diff import generate_diff


@pytest.fixture
def result_for_deap():
    with open('tests/fixtures/right_answer_json.json', "r") as read_file:
        return json.load(read_file)


def test_json():
    assert generate_diff('tests/fixtures/file_deap1.json', 'tests/fixtures/file_deap1.json', "json") == ''


def test_json(result_for_deap):
    res = generate_diff('tests/fixtures/file_deap1.json', 'tests/fixtures/file_deap2.json', "json")
    assert res == '{0}\n'.format(json.dumps(result_for_deap, indent=4))