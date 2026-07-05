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
    List<String> ans = new ArrayList<>();
    void fn(TreeNode root, StringBuilder temp) {
        if (root == null) {
            return;
        }
        StringBuilder curr = new StringBuilder(temp);

        if (root.left == null && root.right == null) {
            curr.append(Integer.toString(root.val));
            this.ans.add(new StringBuilder(curr).toString());
        }
        else {
            curr.append(Integer.toString(root.val)+"->");
        }
        fn( root.left,  curr);
        fn( root.right,  curr);

    }
    public List<String> binaryTreePaths(TreeNode root) {
        fn(root, new StringBuilder());
        return this.ans;
    }
}