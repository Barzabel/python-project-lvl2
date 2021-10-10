import pytest
from gendiff.gen_diff import generate_diff


@pytest.fixture
def result():
    return '{\n    age: 35\n  + cat: True\n    children: True\n    firstName: Jane\n    hobbies: False\n  - lalala: 1\n  - lastName: Doe\n  + lastName: andr\n}'



def test_json(result):
    assert generate_diff('tests/fixtures/1.json', 'tests/fixtures/2.json') == result

def test_yaml(result):
    assert generate_diff('tests/fixtures/1.yaml', 'tests/fixtures/2.yml') == result

