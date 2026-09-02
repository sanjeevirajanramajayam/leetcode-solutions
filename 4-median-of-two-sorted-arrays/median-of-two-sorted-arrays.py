class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        low = 0
        high = len(A) - 1
        total = len(A) + len(B)
        half = total
        half //= 2

        while True:
            mid = (low + high) // 2
            print(mid)
            j = half - (mid + 1) - 1
            Aleft = A[mid] if mid >= 0 else float('-inf')
            Aright = A[mid + 1] if mid + 1 < len(A) else float('inf')
            Bleft = B[j] if j>= 0 else float('-inf')
            Bright = B[j + 1] if j + 1 < len(B) else float('inf')  

            if (Aleft <= Bright and Bleft <= Aright):
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif (Aleft > Bright):
                high = mid - 1
            else:  
                low = mid + 1
        return -1