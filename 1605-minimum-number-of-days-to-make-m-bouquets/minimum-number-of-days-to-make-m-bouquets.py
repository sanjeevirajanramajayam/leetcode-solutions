class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def fn(day):
            bt = 0
            cf = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= day:
                    cf += 1
                else:
                    cf = 0
                if cf == k:
                    bt += 1
                    cf = 0
            return bt
        
        low = min(bloomDay)
        high = max(bloomDay)
        if len(bloomDay) < m * k:
            return -1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            print(low, high, fn(mid))
            if fn(mid) >= m:
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1
        return ans