class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(A) > len(B):
            B, A = A, B
        half = len(A) + len(B)
        totalLen = half
        half //= 2
        l = 0
        r = len(A) - 1
        while True:
            mid = (l + r) // 2
            longMid = half - mid - 2

            if mid >= 0:
                Aleft = A[mid]
            else:
                Aleft = float('-inf')
            
            if (mid + 1) < len(A):
                Aright = A[mid + 1]
            else:
                Aright = float('inf')
            
            if longMid >= 0:
                Bleft = B[longMid]
            else:
                Bleft = float('-inf')
            
            if longMid + 1 < len(B):
                Bright = B[longMid + 1]
            else:
                Bright = float('inf')
            
            if Aleft <= Bright and Bleft <= Aright:
                if totalLen % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                r = mid - 1
            else:
                l = mid + 1
