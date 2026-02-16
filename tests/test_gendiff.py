import os
from gendiff import generate_diff

FIXTURES_PATH = 'tests/test_data'


def get_fixture_path(filename):
    return os.path.join(FIXTURES_PATH, filename)


def read_file(filename):
    with open(get_fixture_path(filename), 'r') as f:
        return f.read()


def test_generate_diff():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_file('expected_result.txt').rstrip('\n')

    result = generate_diff(file1, file2).rstrip('\n')

    assert result == expected

