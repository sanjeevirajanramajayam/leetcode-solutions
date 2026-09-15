"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        curr = root
        if not root:
            return
        next = root.left
        while curr and next:
            next = curr.left
            if curr.left:
                curr.left.next = curr.right
                print(curr.val, next.val)
            while curr.next:
                if curr.right:
                    curr.right.next = curr.next.left
                curr = curr.next
                if curr.left:
                    curr.left.next = curr.right
            curr = next

        return root