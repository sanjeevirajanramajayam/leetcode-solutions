# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        ans = ""
        def preorder(root):
            nonlocal ans
            if root == None:
                return None
            
            ans += str(root.val) + ","

            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ans

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data == "":
            return None
        data = list(map(int, data.split(",")[:-1]))
        # print(data)
        index = 0
        def build(left, right):
            nonlocal index
            if index >= len(data):
                return None

            if not (left <= data[index] <= right):
                return None
            
            node = TreeNode(data[index])
            # print(node.val)
            index += 1
            node.left = build(left, node.val)
            # print(node.left)
            node.right = build(node.val, right)
            # print(node.right)
            return node
        return build(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans