# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left
        # print([x.val for x in self.stack])

    def next(self):
        """
        :rtype: int
        """
        currNode = self.stack.pop()
        curr = currNode.right
        if curr:
            self.stack.append(curr)
        while curr and curr.left:
            self.stack.append(curr.left)
            curr = curr.left
        # print([x.val for x in self.stack])
        return currNode.val
        
            

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()