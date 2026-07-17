class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasCost = []
        for i in range(len(gas)):
            gasCost.append(gas[i] - cost[i])
        
        if sum(gasCost) < 0:
            return -1
        print(gasCost)
        currSum = 0
        maxGas = float('-inf')
        ans = 0
        for i in range(len(gasCost)):
            if currSum == 0:
                ans = i
            currSum += gasCost[i]
            maxGas = max(maxGas, currSum)
            if currSum < 0:
                currSum = 0 
        print(maxGas)
        return ans