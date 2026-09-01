class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        visited = set()
        if n == 1:
            return 1
        n -= 2
        while n >= 0:
            # print(heap)
            val = heapq.heappop(heap)
                # continue
            for factor in [2, 3, 5]:
                if val * factor not in visited:
                    heapq.heappush(heap, val * factor)

                visited.add(val * factor)
            # print(heap)
            n -= 1
        return heap[0]