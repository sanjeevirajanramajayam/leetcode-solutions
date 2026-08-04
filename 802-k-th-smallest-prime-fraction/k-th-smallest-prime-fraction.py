class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        heap = []
        for i in range(len(arr)):
            heapq.heappush(heap, (arr[i] / arr[len(arr) - 1], i, len(arr) - 1, arr[i], arr[len(arr) - 1]))
        while k > 0:
            # print(heap)
            fraction, numerator, denominator, _, _ = heapq.heappop(heap)
            if denominator - 1 >= 0:
                heapq.heappush(heap, (arr[numerator]/ arr[denominator - 1], numerator, denominator - 1, arr[numerator], arr[denominator - 1]))
            k -= 1
            # print(heap)
        return [arr[numerator], arr[denominator]]