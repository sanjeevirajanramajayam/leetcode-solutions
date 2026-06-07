class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.dummyFront = ListNode(-1)
        self.dummyRear = ListNode(-1)
        self.dummyFront.next = self.dummyRear
        self.dummyRear.prev = self.dummyFront
        self.size = k
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.size > 0: 
            newNode = ListNode(value)
            prevNode = self.dummyRear.prev
            newNode.next = prevNode.next
            self.dummyRear.prev = newNode
            prevNode.next = newNode
            newNode.prev = prevNode
            self.size -= 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.size != self.k:
            currNode = self.dummyFront.next
            currNode.prev.next = currNode.next
            currNode.next.prev = currNode.prev
            del currNode
            self.size += 1
            return True
        else:
            return False
    def Front(self) -> int:
        if self.dummyFront.next != self.dummyRear:
            return self.dummyFront.next.val
        else:
            return -1

    def Rear(self) -> int:
        if self.dummyRear.prev != self.dummyFront:
            return self.dummyRear.prev.val
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.size == self.k

    def isFull(self) -> bool:
        return self.size == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()