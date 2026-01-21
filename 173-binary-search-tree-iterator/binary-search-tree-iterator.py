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
        self.root = root
        self.stack = [self.root]
        rootNode = self.root
        while rootNode and rootNode.left:
            self.stack.append(rootNode.left)
            rootNode = rootNode.left
    def next(self):
        """
        :rtype: int
        """
        # print([x.val for x in self.stack])
        node = self.stack.pop()
        if node.right:
            rightNode = node.right
            self.stack.append(rightNode)
            while rightNode and rightNode.left:
                self.stack.append(rightNode.left)
                rightNode = rightNode.left
        # print([x.val for x in self.stack])
        return node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        # print([x.val for x in self.stack])
        return self.stack != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()