class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        for i in nums:
            heapq.heappush(heap, int(i))
            if len(heap) > k:
                heapq.heappop(heap)
        # print(heap)
        return str(heap[0])