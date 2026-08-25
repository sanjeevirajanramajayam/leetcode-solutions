class Node:
    def __init__(self, freq):
        self.freq = freq
        self.prev = None
        self.next = None
        self.keys = set()

class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.char_map = {}

    def inc(self, key: str) -> None:
        if key in self.char_map:
            node = self.char_map[key]
            node.keys.remove(key)
            freq = node.freq
            prevNode = node.prev
            if node.next == self.tail or node.next.freq != freq + 1:
                newNode = Node(freq + 1)
                newNode.keys.add(key)

                nextNode = node.next

                newNode.prev = node
                newNode.next = nextNode

                node.next = newNode
                nextNode.prev = newNode

                self.char_map[key] = newNode
            else:
                nextNode = node.next
                nextNode.keys.add(key)

                self.char_map[key] = nextNode
            
            if not node.keys:
                self.removeNode(node)
        else:
            first_node = self.head.next

            if first_node == self.tail or first_node.freq > 1:
                newNode = Node(1)
                newNode.keys.add(key)

                newNode.prev = self.head
                self.head.next = newNode

                newNode.next = first_node
                first_node.prev = newNode

                self.char_map[key] = newNode
            else:
                first_node.keys.add(key)
                self.char_map[key] = first_node


    def dec(self, key: str) -> None:
        if key not in self.char_map:
            return
        
        node = self.char_map[key]
        node.keys.remove(key)
        freq = node.freq
        if freq == 1:
            del self.char_map[key]
        else:
            prev_node = node.prev
            if prev_node == self.head or prev_node.freq != freq - 1:
                newNode = Node(freq - 1)
                newNode.keys.add(key)

                newNode.prev = prev_node
                newNode.next = node

                prev_node.next = newNode
                node.prev = newNode

                self.char_map[key] = newNode
            else:
                prev_node.keys.add(key)
                self.char_map[key] = prev_node

        if not node.keys:
            self.removeNode(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        else:
            return next(
                iter(self.tail.prev.keys)
            )

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        else:
            return next(
                iter(self.head.next.keys)
            )

    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()