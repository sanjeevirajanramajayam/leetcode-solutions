class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        newArr = [gas[i] - cost[i] for i in range(len(cost))]
        currSum = 0
        maxSum = 0
        start = 0
        print(newArr)
        for i in range(len(gas)):
            if currSum == 0:
                start = i
            currSum += newArr[i]
            maxSum = max(maxSum, currSum)

            if currSum < 0:
                # start = i
                currSum = 0
        return start

        