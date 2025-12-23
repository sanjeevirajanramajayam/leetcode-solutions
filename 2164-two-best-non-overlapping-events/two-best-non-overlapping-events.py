class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events = sorted(events, key=lambda x: (x[0], x[1]))
        maxPoints = 0

        suffixList = [0] * len(events)
        suffixList[len(events) - 1] = events[len(events) - 1][2]
        suffixMax = 0
        for i in range(len(events)-2, -1, -1):
            suffixMax = max(suffixMax, events[i + 1][2], events[i][2])
            suffixList[i] = suffixMax

        for i in range(len(events)):
            low = i
            high = len(events) - 1
            index = -1
            while low <= high:
                mid = (low + high) // 2
                if events[mid][0] > events[i][1]:
                    index = mid
                    high = mid - 1
                else:
                    low = mid + 1
            if index == -1:
                maxPoints = max(maxPoints, events[i][2])
            else:
                maxPoints = max(maxPoints, events[i][2] + suffixList[index])
        return maxPoints