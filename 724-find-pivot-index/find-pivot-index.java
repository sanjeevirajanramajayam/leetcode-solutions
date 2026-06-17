class Solution {
    public int pivotIndex(int[] nums) {
        // ArrayLi/st<Integer> arr = new ArrayList<>();
        // arr.add(0);
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            // arr.add(sum);
        }
        int newSum = 0;
        for (int i = 0; i < nums.length; i++){
            sum -= nums[i];
            // System.out.println(newSum + " " + sum);
            if (newSum == sum) {
                return i;
            }
            newSum += nums[i];

        }
        return -1;
    }
}