# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        oddHead = None
        evenHead = None
        evenB = None
        oddB = None
        curr = head
        cnt = 1
        if not head:
            return None
        if not head.next:
            return head
        while curr:
            front = curr.next
            if cnt % 2 == 0:
                if evenHead == None:
                    evenHead = curr
                    evenB = curr
                else:
                    evenHead.next = curr
                    evenHead = evenHead.next
            else:
                if oddHead == None:
                    oddHead = curr
                    oddB = curr
                else:
                    oddHead.next = curr
                    oddHead = oddHead.next
            cnt += 1
            curr = front
        oddHead.next = None
        evenHead.next = None
        oddHead.next = evenB
        return oddB