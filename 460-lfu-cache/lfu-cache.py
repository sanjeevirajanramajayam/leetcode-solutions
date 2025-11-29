class Node:
    def __init__(self, _key, _value):
        self.key = _key
        self.value = _value
        self.freq = 1
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def add_front(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head
        self.size += 1

    def remove_node(self, node):
        nodePrev = node.prev
        nodeNext = node.next
        nodePrev.next = nodeNext
        nodeNext.prev = nodePrev
        self.size -= 1
    
    def pop_last(self):
        if self.size > 0:
            lastNode = self.tail.prev
            self.remove_node(lastNode)
            return lastNode
        return None

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.nodeMap = {}
        self.freqMap = {}
        self.minFreq = 0

    def update_node(self, node):
        freq = node.freq

        self.freqMap[freq].remove_node(node)

        if freq == self.minFreq and self.freqMap[freq].size == 0:
            self.minFreq += 1

        freq += 1
        node.freq = freq

        if freq not in self.freqMap:
            self.freqMap[freq] = DLL()

        self.freqMap[freq].add_front(node) 

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.nodeMap:
            val = self.nodeMap[key].value
            self.update_node(self.nodeMap[key])
            return val
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return

        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.value = value
            self.update_node(node)
            return
        
        if self.size == self.capacity:
            nodeList = self.freqMap[self.minFreq]
            node = nodeList.pop_last()
            del self.nodeMap[node.key]
            self.size -= 1

        node = Node(key, value)
    
        if 1 not in self.freqMap:
            self.freqMap[1] = DLL()

        self.freqMap[1].add_front(node)
        self.nodeMap[key] = node

        self.minFreq = 1
        self.size += 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)