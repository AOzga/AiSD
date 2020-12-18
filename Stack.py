from Lista import LinkedList,Node


class Stack:

    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __repr__(self):
        node = self._storage.head
        ret = ""
        while node is not None:
            ret += str(node.value) + "\n"
            node = node.next
        return ret

    def __len__(self):
        return len(self._storage)

    def push(self,value :int = 0):
        self._storage.push(value)

    def pop(self):
        return self._storage.pop()


stack = Stack()

assert len(stack) == 0


stack.push(3)
stack.push(10)
stack.push(1)

assert len(stack) == 3

top_value = stack.pop()

assert top_value == 1

assert len(stack) == 2

print(stack)