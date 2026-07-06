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
    int ans = 0;
    void fn(TreeNode root, int depth) {
        if (root == null) {
            return;
        }
        this.ans = Math.max(this.ans, depth);
        fn(root.left, depth + 1);
        fn(root.right, depth + 1);
    }
    public int maxDepth(TreeNode root) {
        fn(root, 1);
        return this.ans;
    }
}