class Solution:
    def halveArray(self, nums: List[int]) -> int:
        currSum = sum(nums)
        # print(currSum)
        halve = currSum / 2
        heap = []
        for x in nums:
            heapq.heappush(heap, -x)
        cnt = 0
        while currSum > halve:
            node = heapq.heappop(heap)
            node = node / 2
            currSum += (node)
            heapq.heappush(heap, node)
            # print(currSum, halve, heap, node)
            cnt += 1
        return cnt 