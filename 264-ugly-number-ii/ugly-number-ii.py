class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = 1
        visited = set()
        heap = [ugly]
        for _ in range(n):
            num = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                if num * factor not in visited:
                    visited.add(num * factor)
                    heapq.heappush(heap, num * factor)
        return num