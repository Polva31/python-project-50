def read_file(filepath):
    """Read file content and return as string."""
    with open(filepath, 'r') as f:
        return f.read()