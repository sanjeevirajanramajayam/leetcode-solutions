class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def fn(ind):
            if ind == len(days):
                return 0
            
            temp = ind
            while temp < len(days) and days[ind] + 1 > days[temp]:
                temp += 1
            one = costs[0] + fn(temp)
            temp = ind
            while temp < len(days) and days[ind] + 7 > days[temp]:
                temp += 1
            seven = costs[1] + fn(temp)
            temp = ind
            while temp < len(days) and days[ind] + 30 > days[temp]:
                temp += 1
            thirty = costs[2] + fn(temp)
            return min(one, seven, thirty)

        return fn(0)