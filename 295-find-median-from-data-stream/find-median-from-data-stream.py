class MedianFinder:

    def __init__(self):
        self.smallNums = []
        self.bigNums = []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallNums, -num)
        if self.smallNums and self.bigNums and self.bigNums[0] < -self.smallNums[0]:
            small = -heapq.heappop(self.smallNums)
            large = heapq.heappop(self.bigNums)

            heapq.heappush(self.smallNums, -large)
            heapq.heappush(self.bigNums, small)
        if len(self.smallNums) > len(self.bigNums) + 1:
            heapq.heappush(self.bigNums, -heapq.heappop(self.smallNums))

    def findMedian(self) -> float:
        if len(self.smallNums) > len(self.bigNums):
            return -self.smallNums[0]

        return (-self.smallNums[0] + self.bigNums[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()