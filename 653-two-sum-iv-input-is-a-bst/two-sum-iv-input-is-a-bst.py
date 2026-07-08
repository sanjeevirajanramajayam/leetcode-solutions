# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIteratorF(object):
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

class BSTIteratorR(object):
    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.right
        # print([x.val for x in self.stack])

    def next(self):
        """
        :rtype: int
        """
        currNode = self.stack.pop()
        curr = currNode.left
        if curr:
            self.stack.append(curr)
        while curr and curr.right:
            self.stack.append(curr.right)
            curr = curr.right
        # print([x.val for x in self.stack])
        return currNode.val
        
            

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        bstf = BSTIteratorF(root)
        bstr = BSTIteratorR(root)

        lp = bstf.next()
        rp = bstr.next()

        while lp < rp:
            sumP = lp + rp
            if sumP == k:
                return True
            if sumP > k:
                rp = bstr.next()
            else:
                lp = bstf.next()
        return False

