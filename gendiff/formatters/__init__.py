from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def apply_formatter(diff, format_name='stylish'):
    """Apply formatter by name."""
    if format_name == 'stylish':
        return format_stylish(diff)
    if format_name == 'plain':
        return format_plain(diff)
    if format_name == 'json':
        return format_json(diff)
    raise ValueError(f"Unknown format: {format_name}")
