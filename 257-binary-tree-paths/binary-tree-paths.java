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
    List<String> a = new ArrayList<>();
    public void build(TreeNode root, StringBuilder s) {
        if (root == null) {
            return;
        }
        StringBuilder curr = new StringBuilder(s);
        if (root.left == null && root.right == null) {
            this.a.add(curr.append(Integer.toString(root.val)).toString());
            return;
        }
        build(root.left, new StringBuilder(curr).append(Integer.toString(root.val) + "->"));
        build(root.right, new StringBuilder(curr).append(Integer.toString(root.val) + "->"));
    }
    public List<String> binaryTreePaths(TreeNode root) {
        build(root, new StringBuilder());
        return a;
    }
}