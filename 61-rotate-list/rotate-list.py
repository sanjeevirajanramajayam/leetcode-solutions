# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        length = 0

        if not head:
            return head
        
        if not head.next:
            return head
        
        prev = None
        while curr:
            prev = curr
            curr = curr.next
            length += 1
        
        k = k % length

        prev.next = head

        for i in range(length - k):
            prev = prev.next
        
        front = prev.next
        prev.next = None
        
        return front
        
