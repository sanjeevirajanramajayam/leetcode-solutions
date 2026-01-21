# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        class BSTIterator:
            def __init__(self, root, reverse):
                self.root = root
                self.stack = [root]
                self.reverse = reverse
                curr = root
                if not self.reverse:
                    while root and root.left:
                        self.stack.append(root.left)
                        root = root.left
                else:
                    while root and root.right:
                        self.stack.append(root.right)
                        root = root.right
            
            def next(self):
                node = self.stack.pop()
                if not self.reverse:
                    if node.right:
                        rightNode = node.right
                        self.stack.append(rightNode)
                        while rightNode and rightNode.left:
                            self.stack.append(rightNode.left)
                            rightNode = rightNode.left
                else:
                    if node.left:
                        leftNode = node.left
                        self.stack.append(leftNode)
                        while leftNode and leftNode.right:
                            self.stack.append(leftNode.right)    
                            leftNode = leftNode.right             
                return node.val
        l = BSTIterator(root, False)
        r = BSTIterator(root, True)

        lPointer = l.next()
        rPointer = r.next()

        while lPointer < rPointer:
            sumP = lPointer + rPointer
            if sumP == k:
                return True
            elif sumP > k:
                rPointer = r.next()
            else:
                lPointer = l.next()
        return False

