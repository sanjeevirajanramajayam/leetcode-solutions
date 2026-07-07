class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int l = 0;
        int r = 0;
        int currentSum = 0;
        int minv = Integer.MAX_VALUE;
        while (r < nums.length) {
            currentSum += nums[r];
            while (currentSum >= target) {
                minv = Math.min(minv, r - l + 1);
                currentSum -= nums[l];
                l += 1;
            }
            r += 1;
        }
        if (minv == Integer.MAX_VALUE) {
            return 0;
        }
        return minv;
    }
}