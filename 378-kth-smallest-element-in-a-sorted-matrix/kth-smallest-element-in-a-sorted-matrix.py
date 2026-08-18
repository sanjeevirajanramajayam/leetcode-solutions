class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(min(len(matrix), k)):
            heapq.heappush(heap, (matrix[i][0], 0, i))
        for i in range(k-1):
            val, j, i = heapq.heappop(heap)
            if j + 1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j + 1], j + 1, i))
            # print(heap)
        return heap[0][0]
