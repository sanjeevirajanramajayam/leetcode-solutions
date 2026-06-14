# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        prev = slow
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        
        prev = None
        curr = slow 

        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        maxv = float('-inf')
        curr = head
        while prev:
            maxv = max(maxv, prev.val + curr.val)
            prev = prev.next
            curr = curr.next

        return maxv