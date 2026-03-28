import json
import yaml


def parse_json(content):
    return json.loads(content)


def parse_yaml(content):
    return yaml.safe_load(content)


def get_parser(file_extension):
    parsers = {
        '.json': parse_json,
        '.yml': parse_yaml,
        '.yaml': parse_yaml,
    }
    return parsers.get(file_extension)


def parse_file(content, file_extension):
    parser = get_parser(file_extension)
    if not parser:
        raise ValueError(f"Unsupported file extension: {file_extension}")
    return parser(content)
