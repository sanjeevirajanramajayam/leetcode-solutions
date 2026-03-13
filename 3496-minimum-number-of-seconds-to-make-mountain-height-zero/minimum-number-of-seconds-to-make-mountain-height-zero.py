class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        
        def valid_time(time):
            htSum = 0
            for wt in workerTimes:
                ht = int(float(-1 + math.sqrt(1 + ((8 * time) / float(wt)))) / 2)
                htSum += ht
            return htSum

        low = 1
        high = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if valid_time(mid) >= mountainHeight:
                ans = mid
                high = mid - 1
            elif valid_time(mid) < mountainHeight:
                low = mid + 1

        return ans

        # for i in range(max(workerTimes), 10 ** 5):
        #     if valid_time(i):
        #         return i