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

public class Pair {
    TreeNode n;
    int i;
    Pair(TreeNode n, int i) {
        this.n = n;
        this.i = i;
    }
    @Override
    public String toString() {
        return "(" + this.n.val + " " + this.i + ")"; 
    }
}

class Solution {
    int ans = 0;
    void levelorder(TreeNode root) {
        ArrayDeque<Pair> ad = new ArrayDeque<>();
        ad.offer(new Pair(root, 0));
        while (!(ad.isEmpty())) {
            int qLen = ad.size();
            while (qLen-- > 0) {
                Pair p = ad.poll();
                if (p.n.left != null) {
                    ad.offer(new Pair(p.n.left, p.i * 2 + 1));
                }
                if (p.n.right != null) {
                    ad.offer(new Pair(p.n.right, p.i * 2 + 2));
                }
            }
            System.out.println(ad);
            int mini = Integer.MAX_VALUE;
            int maxi = Integer.MIN_VALUE;
            for (Pair p: ad ) {
                mini = Math.min(mini, p.i);
                maxi = Math.max(maxi, p.i);
            }
            if (mini == Integer.MAX_VALUE) {
                mini = 0;
            }
            if (maxi == Integer.MIN_VALUE) {
                maxi = 0;
            }
            this.ans = Math.max(this.ans, maxi - mini + 1);

        }
    }
    public int widthOfBinaryTree(TreeNode root) {
        levelorder(root);
        return this.ans;
    }
}