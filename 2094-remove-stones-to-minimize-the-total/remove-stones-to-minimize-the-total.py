class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for x in piles:
            heapq.heappush(heap, -x)
        
        while k > 0:
            n = heapq.heappop(heap)
            n = n // 2
            heapq.heappush(heap, n)
            k -= 1
        
        return -sum(heap)