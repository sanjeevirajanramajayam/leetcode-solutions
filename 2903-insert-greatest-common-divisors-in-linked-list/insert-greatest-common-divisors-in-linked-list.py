# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oldHead = head
        while head and head.next:
            newNode = ListNode(math.gcd(head.val, head.next.val))
            front = head.next
            head.next = newNode
            newNode.next = front
            head = front
        return oldHead