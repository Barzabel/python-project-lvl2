import pytest
from gendiff.gen_diff import generate_diff

def test_one():
	generate_diff('tests/fixtures/1.json', 'tests/fixtures/2.json')
	assert True
