# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums = set(nums)
        prev = None

        fast = head
        while fast:
            if fast.val in nums:
                print(fast.val)
                if fast == head:
                    head = head.next
                    fast = head
                    prev = None
                else:
                    prev.next = fast.next
                    fast = fast.next
            else:
                prev = fast
                fast = fast.next
        # if fast.val in nums:
        #     prev.next = None
        return head
