# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hashmap = {}
        children = set()
        for parent, child, isLeft in descriptions:
            if parent not in hashmap:
                hashmap[parent] = TreeNode(parent)
            if child not in hashmap:
                hashmap[child] = TreeNode(child)
            
            if isLeft == 1:
                hashmap[parent].left = hashmap[child]
            else:
                hashmap[parent].right = hashmap[child]
            
            children.add(child)
        
        for x in hashmap:
            if x not in children:
                return hashmap[x]

        # return hashmap[list(currParent)[0]]
