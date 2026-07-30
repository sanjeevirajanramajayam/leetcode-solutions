class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                heapq.heappush(maxHeap, -matrix[i][j])
                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)
        return -maxHeap[0]