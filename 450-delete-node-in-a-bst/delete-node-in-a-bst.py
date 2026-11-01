# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        def fn(node, key):
            if node == None:
                return None 
            
            if node.val > key:
                node.left = fn(node.left, key)
            elif node.val < key:
                node.right = fn(node.right, key)
            else:
                if not node.left and not node.right:
                    return None 
                if node.left and not node.right:
                    return node.left 
                if node.right and not node.left:
                    return node.right 
                
                sucessor = node.right 
                while sucessor.left:
                    sucessor = sucessor.left
                
                node.val = sucessor.val
                # print(fn(sucessor, sucessor.val))
                node.right = fn(node.right, sucessor.val)
                return node
            return node
        return fn(root, key)