/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    TreeNode build (int[] inorder, int[] postorder, int inStart, int inEnd, int postStart, int postEnd, HashMap<Integer, Integer> m) {
        if (inStart > inEnd || postStart > postEnd) {
            return null;
        }
        TreeNode root = new TreeNode(postorder[postEnd]);
        int inIdx = m.get(postorder[postEnd]);
        int rightSize = inEnd - inIdx;  
        root.left = build(inorder, postorder, inStart, inIdx - 1, postStart, postEnd - rightSize - 1, m);
        root.right = build(inorder, postorder, inIdx + 1, inEnd, postEnd - rightSize, postEnd - 1 , m);
        return root;
    }
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        HashMap<Integer, Integer> m = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            m.put(inorder[i], i);
        }
        return build(inorder, postorder, 0, inorder.length - 1, 0, postorder.length - 1, m);
    }
}