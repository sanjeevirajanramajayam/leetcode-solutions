class Solution { 
    public int fn(int i, int j, List<List<Integer>> triangle, int n, Integer[][] memo) {
        if (i < n) {
            if (j < triangle.get(i).size()) {
                
                if (memo[i][j] != null) {
                    return memo[i][j];
                }


                int mini1 = Integer.MAX_VALUE;
                int mini2 = Integer.MIN_VALUE;

                mini1 = fn(i + 1, j, triangle, n, memo);
                mini2 = fn(i + 1, j + 1, triangle, n, memo);

                int mini3 = Math.min(mini1, mini2);
                memo[i][j] = triangle.get(i).get(j) + mini3;
                return triangle.get(i).get(j) + mini3;
                
            }
            else {
                return 0;
            }
        }
        else {
            return 0;
        }
    }
    public int minimumTotal(List<List<Integer>> triangle) {
        Integer[][] memo = new Integer[triangle.size()][triangle.size()];
        // for (int[] a : memo) {
        //     Arrays.fill(a, -1);
        // }
        // System.out.println(Arrays.deepToString(memo));
        return fn(0, 0, triangle, triangle.size(), memo);
    }
}