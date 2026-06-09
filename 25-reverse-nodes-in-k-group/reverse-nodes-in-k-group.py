# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            while head:
                front = head.next
                head.next = prev
                prev = head
                head = front
            return prev
        
        temp = head
        while temp:
            kth = temp
            
            for i in range(k - 1):
                if kth:
                    kth = kth.next
            
            if kth == None:
                #logic
                break
            
            nextNode = kth.next
            kth.next = None

            revHead = reverse(temp)
            
            temp.next = nextNode

            if temp == head:
                head = revHead
                prevNode = temp
            else:
                prevNode.next = revHead
                prevNode = temp

            temp = nextNode
        return head