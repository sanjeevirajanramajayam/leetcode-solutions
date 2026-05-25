class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def isSubsetSum (arr, target):
            dp = [[False for i in range(target + 1)] for j in range(len(arr) + 1)]
            prev = [False for i in range(target + 1)] 
            dp = [False for i in range(target + 1)] 
            
            prev[0] = True
            dp[0] = True
            if arr[0] <= target:
                dp[arr[0]] = True
                prev[arr[0]] = True
            
            for i in range(1, len(arr)):
                for j in range(1, target + 1):
                    take = False
                    if j >= arr[i]:
                        take = prev[j - arr[i]]
                    not_take = prev[j]
                    dp[j] = take or not_take
                prev = dp[:]
            # print(dp, prev)
            return dp[target]
        arrSum = sum(nums)
        if arrSum % 2 == 1:
            return False
        return isSubsetSum(nums, arrSum // 2)