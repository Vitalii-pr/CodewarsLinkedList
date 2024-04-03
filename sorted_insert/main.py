class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    insertion = Node(data)
    if head is None or head.data > data:
        insertion.next = head
        return insertion

    current = head

    while current.next and current.next.data < data:
        current = current.next

    insertion.next = current.next
    current.next = insertion

    return head
