class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            missing = arr[mid] - (mid + 1)

            if missing >= k:
                high = mid - 1
            else:
                low = mid + 1

        return high + k + 1