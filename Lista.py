from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    head: Node
    tail: Node

    def __init__(self, head=None):
        self.head = head
        self.tail = None

    def __repr__(self):
        hold = self.head
        ret = ''
        while hold:
            ret += f'{hold.value}'
            if hold.next:
                ret += ' -> '
            hold = hold.next
        return ret

    def __len__(self):
        ret = 1
        node = self.head

        if self.head is None:
            return 0

        while node.next is not None:
            ret += 1
            node = node.next

        return ret

    def push(self, value: Any):
        _ = Node(value, self.head)
        self.head = _
        if self.tail is None:
            self.tail = self.head

    def append(self, value: Any):
        if self.head is None:
            self.push(value)
        else:
            _ = Node(value)
            self.tail.next = _
            self.tail = _

    def node(self, at: int = 0):
        node = self.head
        for i in range(at):
            node = node.next
        return node

    def insert(self, value, after):
        _ = Node(value)
        _.next = after.next
        after.next = _

        if after == self.tail:
            self.tail = _

    def pop(self):
        nodetopop = self.head
        if self.head.next is not None:
            self.head = self.head.next
        else: self.head = None
        nodetopop.next = None
        return nodetopop.value

    def remove_last(self) -> Node:
        removedlast = self.tail
        count = self.head

        while count.next is not self.tail:
            count = count.next

        self.tail = count
        count.next = None

        return removedlast.value

    def remove(self, node: Node):
        if node == self.tail:
            return 0
        elif node.next == self.tail:
            self.tail = node
            node.next = None
        else:
            node.next = node.next.next
            node.next.next = None



#def test():
    # list_ = LinkedList()
    #
    # assert list_.head == None
    #
    # list_.push(1)
    # list_.push(0)
    #
    # assert str(list_) == '0 -> 1'
    #
    # list_.append(9)
    # list_.append(10)
    #
    # print(len(list_))
    #
    # assert str(list_) == '0 -> 1 -> 9 -> 10'
    #
    # middle_node = list_.node(at=1)
    # list_.insert(5, after=middle_node)
    #
    # assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'
    #
    # first_element = list_.node(at=0)
    # returned_first_element = list_.pop()
    #
    # assert first_element.value == returned_first_element
    #
    # last_element = list_.node(at=3)
    # returned_last_element = list_.remove_last()
    #
    # assert last_element.value == returned_last_element
    #
    # assert str(list_) == '1 -> 5 -> 9'
    #
    # second_node = list_.node(at=1)
    # list_.remove(second_node)
    #
    # assert str(list_) == '1 -> 5'

