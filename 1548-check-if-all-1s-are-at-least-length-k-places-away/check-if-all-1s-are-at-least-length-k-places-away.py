class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        space = -1
        for i in nums:
            if i == 1:
                if space == -1:
                    space = 0
                    continue
                elif space < k:
                    return False
                else:
                    space = 0
                    continue
            
            if space != -1:
                space += 1
        return True