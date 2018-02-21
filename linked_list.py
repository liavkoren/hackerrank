class Node(object):
    """ Nodes for doubly-linked lists. """
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

    def __repr__(self):
        nodes = []
        head = self
        while head:
            nodes.append(str(head.data))
            head = head.next
        return u'{self.data}, next: {next}'.format(self=self, next='-> '.join(nodes[1:]))

test = Node(1)
test.next = Node(2, prev_node=test)
test.next.next = Node(4, prev_node=test.next)
test.next.next.next = Node(5, prev_node=test.next.next)


# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list
# Note: Recall that an empty list (i.e., where ) and a list with one element are sorted lists.
def SortedInsert(head, data):
    new_node = Node(data)
    if head is None:
        return new_node

    if data < head.data:
        new_node.next = head
        head.prev = new_node
        return new_node

    # There is at least one node in the list, and it is smaller than data:
    pointer = prev = head
    while pointer:
        if pointer.data < data < getattr(pointer.next, 'data', None):
            next = pointer.next
            pointer.next = new_node
            new_node.prev = pointer
            new_node.next = next
            next.prev = new_node
            return head
        else:
            prev = pointer
            pointer = pointer.next
    # If we get here, we've fallen off the list and prev has a reference to the
    # tail of the list.
    prev.next = new_node
    new_node.prev = prev
    return head


# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list

def Reverse(head):
    def inner(head):
        if head.next is None:
            new_head = head
            new_head.prev = None
            return
        inner(head.next)
        next = head.next
        head.prev = next
        next.next = head

    global new_head
    global old_head
    old_head = head
    new_head = None
    if head is None:
        return head

    inner(old_head)
    new_head.prev = None
    old_head.next = None



def reverse_single(p):
    if p.next is None:
        global head
        head = p
        return

    reverse_single(p.next)
    q = p.next
    q.next = p
    p.next = None
