import os
from gendiff.parsers import parse_file
from gendiff.diff_builder import build_diff
from gendiff.formatters import apply_formatter


def generate_diff(file1_path, file2_path, format_name='stylish'):
    """Generate difference between two files."""
    with open(file1_path, 'r') as f:
        content1 = f.read()
    with open(file2_path, 'r') as f:
        content2 = f.read()
    
    ext1 = os.path.splitext(file1_path)[1].lower()
    ext2 = os.path.splitext(file2_path)[1].lower()
    
    data1 = parse_file(content1, ext1)
    data2 = parse_file(content2, ext2)
    
    diff = build_diff(data1, data2)
    return apply_formatter(diff, format_name)
