# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        s = ""
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                s += "#,"
                continue
            s += f"{node.val},"
            queue.append(node.left)
            queue.append(node.right)
        # print(s)
        return s


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return
        data = data.split(",")[:-1]
        # print(data)
        i = 0        
        root = TreeNode(int(data[i]))
        i += 1
        queue = deque([root])
        while queue:
            # print(queue)
            node = queue.popleft()
            # print(node.val , i)
            if data[i] == "#":
                node.left == None
            else:
                node.left = TreeNode(int(data[i]))
                queue.append(node.left)
            i += 1
            if data[i] == "#":
                node.right == None
            else:
                node.right = TreeNode(int(data[i]))
                queue.append(node.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))