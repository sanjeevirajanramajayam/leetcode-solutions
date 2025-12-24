class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.nodeMap = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.removeNode(node)
            self.appendToHead(node)
            return node.value
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.value = value
            self.removeNode(node)
            self.appendToHead(node)
        else:
            if self.capacity == 0:
                lastNode = self.tail.prev
                self.removeNode(lastNode)
                del self.nodeMap[lastNode.key]
                self.capacity += 1
            newNode = Node(key, value)
            self.appendToHead(newNode)
            self.capacity -= 1
            self.nodeMap[key] = newNode 

    def appendToHead(self, node):
        headNext = self.head.next
        self.head.next = node
        node.next = headNext

        headNext.prev = node
        node.prev = self.head
    
    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)