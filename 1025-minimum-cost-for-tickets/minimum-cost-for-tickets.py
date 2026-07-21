class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def fn(ind):
            if ind == len(days):
                return 0
            
            currDay = days[ind]

            oneDay = currDay + 1
            sevenDay = currDay + 7
            thirtyDay = currDay + 30

            temp = ind
            while temp < len(days) and oneDay > days[temp]:
                temp += 1

            ones = costs[0] + fn(temp)

            temp = ind
            while temp < len(days) and sevenDay > days[temp]:
                temp += 1

            seven = costs[1] + fn(temp)

            temp = ind
            while temp < len(days) and thirtyDay > days[temp]:
                temp += 1
            
            thirty = costs[2] + fn(temp)

            return min(ones, seven, thirty)
        return fn(0)