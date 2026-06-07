# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        dummy = ListNode()
        head = dummy
        while l1 or l2:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            # print(val1, val2, carry)
            disum = val1 + val2 + carry
            if disum > 9:
                carry = disum // 10
                disum -= 10
            else:
                carry = 0
            
            newNode = ListNode(disum )
            dummy.next = newNode
            dummy = dummy.next
        if carry != 0:
            newNode = ListNode(carry)
            dummy.next = newNode

        return head.next
