class Node:
    def __init__(self, _key, _value):
        self.key = _key
        self.value = _value
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.map = {}

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def deleteNode(self, nodeRef):
        nodeRefPrev = nodeRef.prev
        nodeRefNext = nodeRef.next
        nodeRefPrev.next = nodeRefNext
        nodeRefNext.prev = nodeRefPrev

    def addToHead(self, nodeRef):
        HeadNext = self.head.next
        self.head.next = nodeRef
        nodeRef.next = HeadNext
        HeadNext.prev = nodeRef
        nodeRef.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            val = self.map[key].value
            self.deleteNode(self.map[key])
            self.addToHead(self.map[key])
            return val
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self.map:
            node = self.map[key]
            node.value = value
            self.deleteNode(self.map[key])
            self.addToHead(self.map[key])
            return

        if len(self.map) == self.capacity:
            lastNode = self.tail.prev
            self.deleteNode(lastNode)
            del self.map[lastNode.key]
        
        newNode = Node(key, value)
        self.addToHead(newNode)
        self.map[newNode.key] = newNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)