# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        dummyNode.next = head

        startNode = dummyNode

        for i in range(left):
            prev = startNode
            startNode = startNode.next
        
        prev.next = None
        old = startNode
        prev2 = None
        for i in range(right - left + 1):
            front = startNode.next
            startNode.next = prev2
            prev2 = startNode
            startNode = front
        
        # prev2.next = None
        
        prev.next = prev2
        old.next = startNode
        # old.next = 
        return dummyNode.next
