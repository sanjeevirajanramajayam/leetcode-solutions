class Solution(object):
    def longestArithmetic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = 0
        diff = None
        maxLen = 0
        for r in range(1, len(nums)):
            curDiff = nums[r] - nums[r - 1]
            # print(curDiff, nums[r], nums[r - 1])
            if diff == None:
                diff = curDiff

            if curDiff == diff:
                maxLen = max(maxLen, r - l + 1)
                # print(maxLen)
                continue
            
            temp_r = r
            newDiff = curDiff
            # print(temp_r, newDiff)
            cur = nums[temp_r - 1] + diff
            while temp_r + 1 < len(nums) and (nums[temp_r + 1] - cur == diff):
                cur = nums[temp_r]
                temp_r += 1
                # prin./t("temp", temp_r)
            maxLen = max(maxLen, temp_r - l + 1)
            l = r - 1
            diff = curDiff 

        nums = nums[::-1]
        l = 0
        diff = None
        for r in range(1, len(nums)):
            curDiff = nums[r] - nums[r - 1]
            # print(curDiff, nums[r], nums[r - 1])
            if diff == None:
                diff = curDiff

            if curDiff == diff:
                maxLen = max(maxLen, r - l + 1)
                # print(maxLen)
                continue
            
            temp_r = r
            newDiff = curDiff
            # print(temp_r, newDiff)
            cur = nums[temp_r - 1] + diff
            while temp_r + 1 < len(nums) and (nums[temp_r + 1] - cur == diff):
                cur = nums[temp_r + 1]
                temp_r += 1
                # prin./t("temp", temp_r)
            maxLen = max(maxLen, temp_r - l + 1)
            l = r - 1
            diff = curDiff 

        return maxLen