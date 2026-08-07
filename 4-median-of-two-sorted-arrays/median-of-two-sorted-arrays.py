class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        low = 0
        high = len(A) - 1
        totalLen = len(A) + len(B)
        half = totalLen // 2
        while True:
            mid = (low + high) // 2
            j = half - mid - 2
            if mid + 1 >= len(A):
                Aright = float('inf')
            else:
                Aright = A[mid + 1]

            if mid < 0:
                Aleft = float('-inf')
            else:
                Aleft = A[mid]

            if j + 1 >= len(B):
                Bright = float('inf')
            else:
                Bright = B[j + 1]

            if j < 0:
                Bleft = float('-inf')
            else:
                Bleft = B[j]
            # print(Blef/t, Aright, Aleft, Bright)
            if Bleft <= Aright and Aleft <= Bright:
                if totalLen % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                high = mid - 1
            else:
                low = mid + 1