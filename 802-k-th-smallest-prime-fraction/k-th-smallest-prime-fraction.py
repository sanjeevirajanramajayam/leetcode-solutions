class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for i in range(min(len(arr) - 1, k)):
            heapq.heappush(heap, (arr[i] / arr[-1], i, len(arr) - 1))
        
        while k > 0:
            fraction, numerator, denominator = heapq.heappop(heap)
            if denominator - 1 > numerator:
                heapq.heappush(heap, (arr[numerator] / arr[denominator - 1], numerator, denominator - 1))
            k -= 1
            # print(heap)
        return [arr[numerator], arr[denominator]]