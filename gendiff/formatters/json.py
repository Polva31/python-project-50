import json


def format_json(diff):
    """Format diff in JSON format."""
    return json.dumps(diff, indent=2)
