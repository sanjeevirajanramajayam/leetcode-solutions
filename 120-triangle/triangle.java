class Solution {
    int fn(int row, int col, List<List<Integer>> triangle, int ROWS, Integer[][] memo) {
            // System.out.println(row + " " + col);
            int i = row;
            int j = col;
            if (memo[i][j] != null) {
                return memo[i][j];
            }
            if (row + 1 == ROWS) {
                memo[i][j] = triangle.get(row).get(col);
                return triangle.get(row).get(col);
            }
            else {
                int a = triangle.get(row).get(col) + fn(row + 1, col, triangle, ROWS, memo);
                int b = triangle.get(row).get(col) + fn(row + 1, col + 1, triangle, ROWS, memo);
                memo[i][j] = Math.min(a, b);
                return Math.min(a, b);
            }
        }
    public int minimumTotal(List<List<Integer>> triangle) {
        int ROWS = triangle.size();
        Integer[][] memo = new Integer[triangle.size()][triangle.size()];
        return fn(0, 0, triangle, ROWS, memo);
    }
}