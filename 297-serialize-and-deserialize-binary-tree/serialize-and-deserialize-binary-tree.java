/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) {
            return "";
        }
        ArrayDeque<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        StringBuilder sb = new StringBuilder();
        while (!(q.isEmpty())) {
            TreeNode t = q.poll();
            if (t.val == -1001) {
                sb.append("#" + ",");
                continue;
            }
            sb.append(t.val + ",");
            if (t.left == null){
                q.offer(new TreeNode(-1001));
            }
            else {
                q.offer(t.left);
            }

            if (t.right == null){
                q.offer(new TreeNode(-1001));
            }
            else {
                q.offer(t.right);
            }
        }
        // System.out.println(sb.toString());
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data == "") {
            return null;
        }
        String[] strList = data.split(",");
        int i = 0;
        ArrayDeque<TreeNode> q = new ArrayDeque<>();
        TreeNode root = new TreeNode(Integer.parseInt(strList[i]));
        q.offer(root);
        while (!q.isEmpty()) {
            TreeNode t = q.poll();
            if (strList[++i].equals("#")) {
                t.left = null;
            }
            else {
                t.left = new TreeNode(Integer.parseInt(strList[i]));
                q.offer(t.left);
            }
            if (strList[++i].equals("#")) {
                t.right = null;
            }
            else {
                t.right = new TreeNode(Integer.parseInt(strList[i]));
                q.offer(t.right);
            }
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));