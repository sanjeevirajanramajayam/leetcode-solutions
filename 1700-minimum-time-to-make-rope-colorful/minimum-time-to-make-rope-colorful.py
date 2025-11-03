class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        min_cost = 0
        max_group = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i - 1] == colors[i]:
                min_cost += min(max_group, neededTime[i])
                max_group = max(max_group, neededTime[i])
            else:
                max_group = neededTime[i]
        return min_cost