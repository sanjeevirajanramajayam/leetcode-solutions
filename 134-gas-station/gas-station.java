class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int[] arr = new int[gas.length];
        int n = gas.length;
        int gasT = 0;
        int costT = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = gas[i] - cost[i];
            gasT += gas[i];
            costT += cost[i];
        }
        if (costT > gasT) {
            return -1;
        }
        int sum = 0;
        int start = 0;
        for (int i = 0; i < n; i++) {
            if (sum == 0) {
                start = i;
            }
            sum += arr[i];
            if (sum < 0) {
                sum = 0;
            }
        }
        return start;
    }
}