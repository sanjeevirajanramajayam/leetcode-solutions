class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
        for i in range(len(arr)):
            if arr[i] > k:
                return k
            k += 1
        return k