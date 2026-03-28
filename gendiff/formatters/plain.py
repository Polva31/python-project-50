def _format_value(value):
    """Format value for plain output."""
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def _process_node(node, path):
    """Process single node and return plain format string."""
    current_path = f"{path}.{node['key']}" if path else node['key']
    
    if node['type'] == 'added':
        return f"Property '{current_path}' was added with value: {_format_value(node['value'])}"
    
    if node['type'] == 'removed':
        return f"Property '{current_path}' was removed"
    
    if node['type'] == 'changed':
        old = _format_value(node['old_value'])
        new = _format_value(node['new_value'])
        return f"Property '{current_path}' was updated. From {old} to {new}"
    
    if node['type'] == 'nested':
        lines = []
        for child in node['children']:
            child_line = _process_node(child, current_path)
            if child_line:
                lines.append(child_line)
        return '\n'.join(lines)
    
    return ''


def format_plain(diff):
    """Format diff in plain format."""
    lines = []
    for node in diff:
        line = _process_node(node, '')
        if line:
            lines.append(line)
    return '\n'.join(lines)
