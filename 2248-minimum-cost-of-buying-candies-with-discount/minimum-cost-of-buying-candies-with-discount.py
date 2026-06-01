class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return sum(cost)
        cost.sort()
        csum = 0
        l = len(cost) - 1
        while l >= 2:
            csum += cost[l]
            csum += cost[l - 1]
            l -= 3
        # l -= 1
        while l >= 0:
            csum += cost[l]
            l-= 1
        return csum
