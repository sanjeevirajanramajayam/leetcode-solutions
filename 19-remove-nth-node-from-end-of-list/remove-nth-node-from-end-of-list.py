# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummyNode = ListNode()
        dummyNode.next = head
        slow = dummyNode
        fast = dummyNode
        for i in range(n + 1):
            fast = fast.next
        # print(fast.val)
        while fast:
            slow = slow.next
            fast = fast.next
        # print(slow.val, fast.val)
        slow.next = slow.next.next
        return dummyNode.next