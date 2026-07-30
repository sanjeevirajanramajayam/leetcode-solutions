class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = 1
        visited = set()
        heap = [ugly]
        for _ in range(n):
            temp = heapq.heappop(heap)
            # temp = heap[0]
            for factor in [2, 3, 5]:
                newNum = temp * factor
                if newNum not in visited:
                    visited.add(newNum)
                    heapq.heappush(heap, newNum)

        return temp