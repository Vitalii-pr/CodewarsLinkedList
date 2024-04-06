class Node:
    def __init__(self):
        self.next = None


def loop_size(node):
    slow, fast = node.next, node.next.next

    while fast != slow:
        slow = slow.next
        fast = fast.next.next

    loop_count = 1
    fast = fast.next
    while fast != slow:
        loop_count += 1
        fast = fast.next
    return loop_count
