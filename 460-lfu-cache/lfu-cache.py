class Node:
    def __init__(self, key, value):
        self.next = None
        self.prev = None
        self.freq = 1
        self.key = key
        self.value = value

class DLL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def appendNode(self, node):
        nextNode = self.head.next
        self.head.next = node
        node.next = nextNode
        nextNode.prev = node
        node.prev = self.head
        self.size += 1

    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.size -= 1
        

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.currentCap = 0
        self.nodeMap = {}
        self.freqMap = {}
        self.minFreq = -1

    def updateNode(self, node):
        freq = node.freq
        DDList = self.freqMap[freq]
        DDList.removeNode(node)

        if freq == self.minFreq and DDList.size == 0:
            self.minFreq += 1
        
        freq += 1
        node.freq = freq

        if freq not in self.freqMap:
            self.freqMap[freq] = DLL()
        
        self.freqMap[freq].appendNode(node)


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.updateNode(node)
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
            self.updateNode(node)
            return

        if self.currentCap == self.capacity:
            minList = self.freqMap[self.minFreq]
            lastNode = minList.tail.prev
            minList.removeNode(lastNode)
            del self.nodeMap[lastNode.key]
            self.currentCap -= 1

        self.minFreq = 1
        self.currentCap += 1
        newNode = Node(key, value)
        if newNode.freq not in self.freqMap:
            self.freqMap[newNode.freq] = DLL()
        self.nodeMap[key] = newNode
        self.freqMap[newNode.freq].appendNode(newNode)
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)