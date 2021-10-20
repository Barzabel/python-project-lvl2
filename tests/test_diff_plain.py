import pytest
from gendiff.gendiff import generate_diff


@pytest.fixture
def result_for_deap():
    print(generate_diff('tests/fixtures/file_deap1.json', 'tests/fixtures/file_deap1.json', "plain"))
    with open('tests/fixtures/right_answer_plain', "r") as read_file:
        return read_file.read()


def test_json():
    assert generate_diff('tests/fixtures/file_deap1.json', 'tests/fixtures/file_deap1.json', "plain") == ''


def test_json(result_for_deap):
    assert generate_diff('tests/fixtures/file_deap1.json', 'tests/fixtures/file_deap2.json', "plain") == result_for_deap
