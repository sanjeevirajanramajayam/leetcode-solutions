class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low = 1
        high = max(bloomDay)
        
        def fn(day):
            b = 0
            f = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= day:
                    f += 1
                    if f == k:
                        b += 1
                        f = 0
                else:
                    f = 0
            return b
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            # print(mid, fn(mid))
            if fn(mid) >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans