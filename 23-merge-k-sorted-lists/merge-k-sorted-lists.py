# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        def mergeList(l1, l2):
            curr = ListNode()
            dummy = curr
            while l1 and l2:
                if l1.val > l2.val:
                    dummy.next = l2
                    dummy = dummy.next
                    l2 = l2.next
                else:
                    dummy.next = l1
                    dummy = dummy.next
                    l1 = l1.next
            
            if l1:
                dummy.next = l1
            
            if l2:
                dummy.next = l2

            return curr.next

        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                # print(i)
                list1 = lists[i]
                if i + 1 >= len(lists):
                    list2 = None
                else:
                    list2 = lists[i + 1]
                newList = mergeList(list1, list2)
                # print(newList)
                mergedList.append(newList)
            # print(mergedList)
            lists = mergedList
            # print(lists)
        if lists:
            return lists[0]
        else:
            return None

                