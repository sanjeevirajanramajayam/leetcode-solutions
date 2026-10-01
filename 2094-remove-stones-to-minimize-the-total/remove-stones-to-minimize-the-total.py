class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        heap = [-x for x in piles]
        heapq.heapify(heap)
        for i in range(k):
            v = heapq.heappop(heap)
            v = v // 2
            heapq.heappush(heap, v)
            # print(heap)
        return -sum(heap)
        