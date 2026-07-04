class Solution {
    public int maxArea(int[] h) {
        int l = 0;
        int r = h.length - 1;
        int maxArea = 0;

        while (l < r) {
            maxArea = Math.max(maxArea, (r - l) * Math.min(h[l], h[r]));
            if (h[r] > h[l] ) {
                l += 1;
            }
            else {
                r -= 1;
            }
        }
    
        return maxArea;
    }
}