/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    TreeNode fn(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) {
            return null;
        }
        TreeNode left = fn(root.left, p, q);
        TreeNode right = fn(root.right, p, q);
        if (root.val == p.val) {
            return p;
        }
        if (root.val == q.val) {
            return q;
        }
        if (left != null && right != null) {
            return root;
        }
        // if (left == null && right == null) {
        //     return null;
        // }
        if (left != null) {
            return left;
        }
        if (right != null) {
            return right;
        }
        return null;
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return fn(root,p,q);
    }
}