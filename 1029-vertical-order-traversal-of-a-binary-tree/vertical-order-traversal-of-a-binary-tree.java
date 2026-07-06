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
    int x;
    int y;
    Pair(TreeNode n, int x, int y) {
        this.n = n;
        this.x = x;
        this.y = y;
    }
    @Override
    public String toString() {
        return "(" + this.n.val + " " + this.x + " " + this.y + ")"; 
    }
}

class Solution {
    List<List<Integer>> ans = new ArrayList<>();

    void levelorder(TreeNode root) {
        ArrayDeque<Pair> ad = new ArrayDeque<>();
        Map<Integer,List<Pair>> m = new TreeMap<>();
        ad.offer(new Pair(root, 0, 0));
        if (!m.containsKey(0)) {
            m.put(0, new ArrayList<>());
        }
        m.get(0).add(new Pair(root, 0, 0));
        while (!(ad.isEmpty())) {
            int qLen = ad.size();
            while (qLen-- > 0) {
                Pair p = ad.poll();
                if (p.n.left != null) {
                    ad.offer(new Pair(p.n.left, p.x + 1, p.y - 1));
                }
                if (p.n.right != null) {
                    ad.offer(new Pair(p.n.right, p.x + 1, p.y + 1));
                }
            }
            // System.out.println(ad);
            // int mini = Integer.MAX_VALUE;
            // int maxi = Integer.MIN_VALUE;
            for (Pair p: ad ) {
                // m.put(p.y, );
                if (!m.containsKey(p.y)) {
                    m.put(p.y, new ArrayList<>());
                }
                m.get(p.y).add(p);
            }
            // if (mini == Integer.MAX_VALUE) {
            //     mini = 0;
            // }
            // if (maxi == Integer.MIN_VALUE) {
            //     maxi = 0;
            // }
            // this.ans = Math.max(this.ans, maxi - mini + 1);
            // System.out.println(m);
        }
        for (var key: m.keySet()){
            ArrayList<Integer> a = new ArrayList<>();
            List<Pair> lp = m.get(key);

            Collections.sort(lp, (ax, bx) -> {
                if (ax.x > bx.x) {
                    return 1;
                }
                else if (ax.x < bx.x) {
                    return -1;
                }
                if (ax.n.val > bx.n.val) {
                    return 1;
                }
                else if (ax.n.val < bx.n.val) {
                    return -1;
                }
                return 0;
            });
            this.ans.add(new ArrayList<>());
            for (Pair p : lp) {
                this.ans.get(ans.size() - 1).add(p.n.val);
            }
        }

    }
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        levelorder(root);
        return ans;
    }
}