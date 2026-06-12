class Solution(object):
    def combinationSum(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        def fn(ind, currSum, arr):
            if currSum == target:
                ans.append(arr[:])
                return True
            
            for i in range(ind, len(nums)):
                if currSum + nums[i] <= target:
                    fn(i, currSum + nums[i], arr + [nums[i]])
        fn(0, 0, [])
        return ans