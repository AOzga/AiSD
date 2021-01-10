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


queue = Queue()
assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2