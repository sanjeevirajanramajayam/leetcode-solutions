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
    int maxVal = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        int test = inorder(root);
        return maxVal;
    }

    int inorder(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = inorder(root.left);
        int right = inorder(root.right);
        maxVal = Math.max(maxVal, left + right);
        return 1 + Math.max(left, right);
    }
}