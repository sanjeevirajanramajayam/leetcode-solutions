class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        A, B = nums1, nums2 
        swapped = False
        if A[0] > B[0]:
            A, B = B, A 
            swapped = True
        heap = []
        for i in range(len(B)):
            heap.append((A[0] + B[i], 0, i))
        heapq.heapify(heap)
        ans = []
        while k > 0:
            add, Aind, Bind = heapq.heappop(heap)
            ans.append([A[Aind], B[Bind]])
            if swapped:
                ans[-1] = ans[-1][::-1]
            if Aind + 1 < len(A):
                heapq.heappush(heap, (B[Bind] + A[Aind + 1], Aind + 1, Bind))        
            k -= 1  
        return (ans)  