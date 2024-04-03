class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def get_nth(node, index):
    if index < 0 or node is None:
        raise IndexError
    node = node
    for i in range(index):
        if node.next:
            node = node.next
        else:
            raise IndexError
    return node