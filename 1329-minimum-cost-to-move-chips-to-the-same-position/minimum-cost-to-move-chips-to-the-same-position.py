class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        oddCount = 0
        evenCount = 0
        for i in position:
            if i % 2 == 0:
                evenCount += 1
            else:
                oddCount += 1
        return min(evenCount, oddCount)