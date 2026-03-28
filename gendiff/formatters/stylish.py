def _format_value(value, depth):
    if isinstance(value, dict):
        lines = ['{']
        for k, v in value.items():
            lines.append(f"{'    ' * (depth + 1)}{k}: {_format_value(v, depth + 1)}")
        lines.append(f"{'    ' * depth}}}")
        return '\n'.join(lines)
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return str(value)


def _process_node(node, depth):
    indent = '    ' * depth
    indent_without_last = indent[:-4] + '  ' if depth > 0 else ''
    
    if node['type'] == 'added':
        return f"{indent_without_last}  + {node['key']}: {_format_value(node['value'], depth + 1)}"
    if node['type'] == 'removed':
        return f"{indent_without_last}  - {node['key']}: {_format_value(node['value'], depth + 1)}"
    if node['type'] == 'unchanged':
        return f"{indent}    {node['key']}: {_format_value(node['value'], depth + 1)}"
    if node['type'] == 'changed':
        old = f"{indent_without_last}  - {node['key']}: {_format_value(node['old_value'], depth + 1)}"
        new = f"{indent_without_last}  + {node['key']}: {_format_value(node['new_value'], depth + 1)}"
        return f"{old}\n{new}"
    if node['type'] == 'nested':
        children = '\n'.join(_process_node(child, depth + 1) for child in node['children'])
        return f"{indent}    {node['key']}: {{\n{children}\n{indent}    }}"
    return ''


def format_stylish(diff):
    result = ['{']
    for node in diff:
        line = _process_node(node, 1)
        if line:
            result.append(line)
    result.append('}')
    return '\n'.join(result)
