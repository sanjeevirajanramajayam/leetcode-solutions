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
        nxt = None
        if not root:
            return

        if curr.left:
            nxt = curr.left
        
        while curr and nxt:
            curr.left.next = curr.right
            # nxt = nxt.next
            if curr.next:
                curr.right.next = curr.next.left

            curr = curr.next
            
            if not curr:
                curr = nxt
                nxt = nxt.left
        return root