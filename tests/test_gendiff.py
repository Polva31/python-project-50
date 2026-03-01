import json
import os

from gendiff import generate_diff

FIXTURES_PATH = 'tests/test_data'


def get_fixture_path(filename):
    return os.path.join(FIXTURES_PATH, filename)


def read_file(filename):
    with open(get_fixture_path(filename)) as f:
        return f.read()


def normalize_json(data):
    return json.dumps(json.loads(data), sort_keys=True, indent=2)


def test_gendiff_json():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_file('expected_result.txt').rstrip('\n')
    result = generate_diff(file1, file2).rstrip('\n')
    assert result == expected


def test_gendiff_yaml():
    file1 = get_fixture_path('file1.yml')
    file2 = get_fixture_path('file2.yml')
    expected = read_file('expected_result.txt').rstrip('\n')
    result = generate_diff(file1, file2).rstrip('\n')
    assert result == expected


def test_gendiff_nested_json():
    file1 = get_fixture_path('file1_nested.json')
    file2 = get_fixture_path('file2_nested.json')
    expected = read_file('expected_nested.txt').rstrip('\n')
    result = generate_diff(file1, file2).rstrip('\n')
    assert result == expected


def test_gendiff_nested_yaml():
    file1 = get_fixture_path('file1_nested.yml')
    file2 = get_fixture_path('file2_nested.yml')
    expected = read_file('expected_nested.txt').rstrip('\n')
    result = generate_diff(file1, file2).rstrip('\n')
    assert result == expected


def test_gendiff_plain_format():
    file1 = get_fixture_path('file1_nested.json')
    file2 = get_fixture_path('file2_nested.json')
    expected = read_file('expected_plain.txt').rstrip('\n')
    result = generate_diff(file1, file2, 'plain').rstrip('\n')
    assert result == expected


def test_gendiff_plain_format_yaml():
    file1 = get_fixture_path('file1_nested.yml')
    file2 = get_fixture_path('file2_nested.yml')
    expected = read_file('expected_plain.txt').rstrip('\n')
    result = generate_diff(file1, file2, 'plain').rstrip('\n')
    assert result == expected


def test_gendiff_json_format():
    file1 = get_fixture_path('file1_nested.json')
    file2 = get_fixture_path('file2_nested.json')
    expected = read_file('expected_json.txt').rstrip('\n')
    result = generate_diff(file1, file2, 'json')
    result_normalized = normalize_json(result)
    expected_normalized = normalize_json(expected)
    assert result_normalized == expected_normalized


def test_gendiff_json_format_yaml():
    file1 = get_fixture_path('file1_nested.yml')
    file2 = get_fixture_path('file2_nested.yml')
    expected = read_file('expected_json.txt').rstrip('\n')
    result = generate_diff(file1, file2, 'json')
    result_normalized = normalize_json(result)
    expected_normalized = normalize_json(expected)
    assert result_normalized == expected_normalized


def test_gendiff_stylish_format_explicit():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_file('expected_result.txt').rstrip('\n')
    result = generate_diff(file1, file2, 'stylish').rstrip('\n')
    assert result == expected
