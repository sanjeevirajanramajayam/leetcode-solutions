class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        low = 0
        high = len(A)

        while low <= high:
            mid = (low + high) // 2

            r2 = mid
            l2 = r2 - 1

            r1 = half - r2
            l1 = r1 - 1

            Aleft  = A[l2] if l2 >= 0 else float('-inf')
            Aright = A[r2] if r2 < len(A) else float('inf')

            Bleft  = B[l1] if l1 >= 0 else float('-inf')
            Bright = B[r1] if r1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0

            elif Aleft > Bright:
                high = mid - 1
            else:
                low = mid + 1
