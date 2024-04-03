def stringify(node):
    return str(node.data) + ' -> ' + stringify(node.next) if node is not None else 'None'