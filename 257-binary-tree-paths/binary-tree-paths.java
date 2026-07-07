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
    ArrayList<String> a = new ArrayList<>();
    public void build(TreeNode root, StringBuilder temp) {
        if (root == null) {
            return;
        }
        if (root.left == null && root.right == null) {
            this.a.add(new StringBuilder(temp).append(root.val).toString());
        }
        build(root.left, new StringBuilder(temp).append(root.val + "->"));
        build(root.right, new StringBuilder(temp).append(root.val + "->"));

    }
    public List<String> binaryTreePaths(TreeNode root) {
        build(root, new StringBuilder());
        return this.a;
    }
}