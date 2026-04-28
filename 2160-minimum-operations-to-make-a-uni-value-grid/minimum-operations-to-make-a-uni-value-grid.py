class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        sortedList = []
        for i in grid:
            for j in i:
                sortedList.append(j)
        sortedList.sort()
        midElement = sortedList[len(sortedList)//2]
        # print(midElement)
        cost = 0
        for i in range(len(sortedList)):
            if (sortedList[i] - sortedList[0]) % x != 0:
                return -1
            cost += abs(midElement - sortedList[i]) // x
            # print(cost, sortedList[i])
        return cost