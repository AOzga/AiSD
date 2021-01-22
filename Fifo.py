from Lista import LinkedList, Node


class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __str__(self):
        ret = ''
        node = self._storage.head
        while node is not None:
            ret += str(node.value)
            if node.next is not None:
                ret += ', '
            node = node.next
        return ret

    def __len__(self):
        return len(self._storage)

    def enqueue(self,value):
        self._storage.append(value)

    def dequeue(self):
        return self._storage.pop()


