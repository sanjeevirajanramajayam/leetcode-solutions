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
        Queue<TreeNode> ad = new LinkedList<>();
        ad.offer(root);
        StringBuilder sb = new StringBuilder();
        while (!ad.isEmpty()) {
            TreeNode node = ad.poll();
            if (node == null) {
                sb.append("#,");
                continue;
            }
            sb.append(node.val + ",");
            ad.offer(node.left);
            ad.offer(node.right);
        }
        // System.out.println(sb.toString());
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data == "") {
            return null;
        }
        Queue<TreeNode> queue = new LinkedList<>();

        String[] strList = data.split(",");
        // System.out.println(Arrays.deepToString(strList));
        List<String> strLis = Arrays.asList(strList);
        Iterator<String> it = strLis.iterator();
        TreeNode root = new TreeNode(Integer.parseInt(it.next()));
        queue.offer(root);
        while (!queue.isEmpty()) {
            // String s = it.next();
            TreeNode node = queue.poll();

            String left = it.next();
            String right = it.next();

            if (left.equals("#")) {

            }
            else {
                node.left = new TreeNode(Integer.parseInt(left));
                queue.offer(node.left);
            }

            if (right.equals("#")) {

            }
            else {
                node.right = new TreeNode(Integer.parseInt(right));
                queue.offer(node.right);
            }
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));