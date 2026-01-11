class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda x: x[1])
        count = 0
        lastTime = float('-inf')
        for i in range(len(intervals)):
            if intervals[i][0] >= lastTime:
                count += 1
                lastTime = intervals[i][1]
        return len(intervals) - count