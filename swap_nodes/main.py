class Node:
    def __init__(self, next=None):
        self.next = next


def swap_pairs(head):
    if head is None or head.next is None:
        return head

    first, head.next = head.next, swap_pairs(head.next.next)
    first.next = head
    return first
