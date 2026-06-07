# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        curr = head
        # print(prev.val, head.val)
        dummy = ListNode()
        while curr:
            temp = curr.next
            if prev.next:
                temp2 = prev.next
            else:
                temp2 = None

            dummy.next = curr
            dummy = dummy.next

            curr.next = prev
            
            dummy = dummy.next

            curr = temp

            prev = temp2

        return dummy.next
