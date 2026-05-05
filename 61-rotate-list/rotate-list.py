# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        if not head.next:
            return head
        def reverse(head, end = None):
            prev = None
            pPrev = None
            node = head
            while node != end:
                if prev:
                    prev.next = pPrev
                pPrev = prev
                prev = node
                node = node.next
            if prev:
                prev.next = pPrev
            return prev
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        k = k % count
        go = count - k
        # print(k, go)

        curr = head
        tempCnt = 0
        tempNode = None
        while curr:
            tempCnt += 1
            curr = curr.next
            if tempCnt == go:
                tempNode = curr
        # print(tempNode.val)

        lastNode = reverse(head, tempNode)
        lastNode3 = None
        curr = lastNode
        while curr.next:
            curr = curr.next
        lastNode2 = reverse(tempNode)
        curr.next = lastNode2
        return reverse(lastNode)