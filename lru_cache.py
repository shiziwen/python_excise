class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None

    def isEmpty(self):
        return not self.tail

    def removeLast(self):
        self.remove(self.tail)

    def remove(self, node):
        if self.head == self.tail:
            self.head, self.tail = None, None
            return

        if node == self.head:
            node.next.prev = None
            self.head = nodex.next
            return

        if node == self.tail:
            node.prev.next = None
            self.tail = node.prev
            return

        node.prev.next = node.next
        node.next.prev = node.prev

    def addFirst(self, node):
        if not self.head:
            self.head = self.tail = node
            node.prev = node.next = None
            return
        
        node.next = self.head
        self.head.prev = node
        self.head = node
        node.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.m = dict()
        self.cache = DoubleLinkedList

    def get(self, key):
        if (key in self.m) and self.m[key]:
            self.cache.remove(self.m[key])
            self.cache.addFirst(self.m[key])
            return self.m[key].val
        else:
            return -1

    def set(self, key, value):
        if key in self.m:
            self.cache.remove(self.m[key])
            self.cache.addFirst(self.m[key])
            self.m[key].val = value
        else:
            node = Node(key, value)
            self.m[key] = node
            self.cache.addFirst(node)
            self.size += 1
            if self.size > self.capacity:
                self.size -= 1
                del self.m[self.cache.tail.key]
                self.cache.removeLast()


