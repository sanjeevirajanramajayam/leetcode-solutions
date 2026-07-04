class Solution {
    public int trap(int[] height) {
        int[] prefixArray = new int[height.length + 1];
        int[] suffixArray = new int[height.length + 1];
        int n = height.length + 1;
        for (int i = 1; i < n; i++) {
            prefixArray[i] = Math.max(prefixArray[i - 1], height[i - 1]);
        }
        for (int i = n - 2; i >= 0; i--) {
            suffixArray[i] = Math.max(suffixArray[i + 1], height[i]);
        }
        // System.out.println(Arrays.toString(prefixArray) + " " + Arrays.toString(suffixArray)); 
        int maxArea = 0;
        for (int i = 0; i < height.length; i++ ){
            maxArea += Math.min(prefixArray[i+1], suffixArray[i]) - height[i];
        }
        return maxArea;
    }
}