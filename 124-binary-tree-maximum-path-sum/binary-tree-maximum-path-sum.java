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
    int ans = Integer.MIN_VALUE;
    int fn(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int lh = fn(root.left);
        int rh = fn(root.right);
        lh = Math.max(lh, 0);
        rh = Math.max(rh, 0);
        this.ans = Math.max(this.ans, lh + rh + root.val);
        return root.val + Math.max(lh, rh);

    }
    public int maxPathSum(TreeNode root) {
        fn(root);
        return this.ans;
    }
}