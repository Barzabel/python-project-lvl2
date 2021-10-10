import pytest
from gendiff.gen_diff import generate_diff

def test_json():
    res = '{\n    age: 35\n  + cat: True\n    children: True\n    firstName: Jane\n    hobbies: False\n  - lalala: 1\n  - lastName: Doe\n  + lastName: andr\n}'
    assert generate_diff('tests/fixtures/1.json', 'tests/fixtures/2.json') == res

def test_yaml():
    res = '{\n    age: 35\n  + cat: True\n    children: True\n    firstName: Jane\n    hobbies: False\n  - lalala: 1\n  - lastName: Doe\n  + lastName: andr\n}'
    assert generate_diff('tests/fixtures/1.yaml', 'tests/fixtures/2.yml') == res

