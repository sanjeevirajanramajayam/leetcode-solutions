class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []
        for i in range(min(k, len(matrix))):
            heapq.heappush(maxHeap, (matrix[i][0], i, 0))
        for _ in range(k - 1):
            val, i, j = heapq.heappop(maxHeap)
            if j + 1 < len(matrix):
                heapq.heappush(maxHeap, (matrix[i][j + 1], i, j + 1))
        return heapq.heappop(maxHeap)[0]

