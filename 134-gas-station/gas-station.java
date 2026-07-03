class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        // int arr[] = new int[gas.length];
        // for (int i = 0; i < gas.length; i++) {
        //     arr[i] = gas[i] - cost[i];
        // }
        int sum = 0;
        int start = 0;
        int nSum = 0;
        for (int i = 0; i < gas.length; i++) {
            if (sum == 0)
                start = i;
            sum += gas[i] - cost[i];
            nSum += gas[i] - cost[i];
            if (sum < 0)
                sum = 0;
        }
        if (nSum < 0)
            return -1;
        return (start);
    }
}