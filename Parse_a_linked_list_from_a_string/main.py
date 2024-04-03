class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def linked_list_from_string(s):
    if s is None:
        return Node(s)
    prev = None
    for i in s.split(' -> ')[-2::-1]:
        head = Node(int(i), prev)
        prev = head
    return prev
