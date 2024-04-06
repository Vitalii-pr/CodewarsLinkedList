class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if head is None or head.next is None:
        raise Exception()

    result = Context(head, head.next)

    first = result.first
    second = result.second

    head = head.next.next

    i = 1
    while True:
        if i & 1:
            first.next = head
            first = first.next
        else:
            second.next = head
            second = second.next
        i += 1
        if head is None:
            break
        head = head.next

    return result
