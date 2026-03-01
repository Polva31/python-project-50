import json
import os

import pytest

from gendiff import generate_diff

FIXTURES_PATH = 'tests/test_data'


def get_fixture_path(filename):
    return os.path.join(FIXTURES_PATH, filename)


def read_file(filename):
    with open(get_fixture_path(filename)) as f:
        return f.read()


def normalize_json(json_str):
    """Normalize JSON string for comparison."""
    return json.dumps(json.loads(json_str), indent=2, sort_keys=True)


def test_generate_diff_json_flat():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_file('expected_result.txt').rstrip('\n')

    result = generate_diff(file1, file2).rstrip('\n')

    assert result == expected


def test_generate_diff_yaml_flat():
    file1 = get_fixture_path('file1.yml')
    file2 = get_fixture_path('file2.yml')
    expected = read_file('expected_result.txt').rstrip('\n')

    result = generate_diff(file1, file2).rstrip('\n')

    assert result == expected


def test_generate_diff_nested_json():
    file1 = get_fixture_path('file1_nested.json')
    file2 = get_fixture_path('file2_nested.json')
    expected = read_file('expected_nested.txt').rstrip('\n')

    result = generate_diff(file1, file2).rstrip('\n')

    assert result == expected


def test_generate_diff_nested_yaml():
    file1 = get_fixture_path('file1_nested.yml')
    file2 = get_fixture_path('file2_nested.yml')
    expected = read_file('expected_nested.txt').rstrip('\n')

    result = generate_diff(file1, file2).rstrip('\n')

    assert result == expected


def test_generate_diff_plain_json():
    file1 = get_fixture_path('file1_nested.json')
    file2 = get_fixture_path('file2_nested.json')
    expected = read_file('expected_plain.txt').rstrip('\n')

    result = generate_diff(file1, file2, 'plain').rstrip('\n')

    assert result == expected


def test_generate_diff_plain_yaml():
    file1 = get_fixture_path('file1_nested.yml')
    file2 = get_fixture_path('file2_nested.yml')
    expected = read_file('expected_plain.txt').rstrip('\n')

    result = generate_diff(file1, file2, 'plain').rstrip('\n')

    assert result == expected


def test_generate_diff_json_format():
    file1 = get_fixture_path('file1_nested.json')
    file2 = get_fixture_path('file2_nested.json')
    expected = read_file('expected_json.txt').rstrip('\n')

    result = generate_diff(file1, file2, 'json')
    result_normalized = normalize_json(result)
    expected_normalized = normalize_json(expected)

    assert result_normalized == expected_normalized


def test_generate_diff_json_format_yaml():
    file1 = get_fixture_path('file1_nested.yml')
    file2 = get_fixture_path('file2_nested.yml')
    expected = read_file('expected_json.txt').rstrip('\n')

    result = generate_diff(file1, file2, 'json')
    result_normalized = normalize_json(result)
    expected_normalized = normalize_json(expected)

    assert result_normalized == expected_normalized


def test_generate_diff_with_format_arg():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_file('expected_result.txt').rstrip('\n')

    result = generate_diff(file1, file2, 'stylish').rstrip('\n')

    assert result == expected


def test_unsupported_format():
    with pytest.raises(ValueError, match="Unknown format"):
        file1 = get_fixture_path('file1.json')
        file2 = get_fixture_path('file2.json')
        generate_diff(file1, file2, 'unknown')
