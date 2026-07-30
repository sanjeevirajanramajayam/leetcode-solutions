class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for i in range(len(arr)):
            heapq.heappush(heap, (arr[i] / arr[-1], i, len(arr) - 1))
        # print(heap)
        while k > 0:
            fraction, i, j = heapq.heappop(heap)
            k -= 1
            if j - 1 > i:
                heapq.heappush(heap, (arr[i] / arr[j - 1], i, j - 1))
                # print(heap)
        return [arr[i], arr[j]]