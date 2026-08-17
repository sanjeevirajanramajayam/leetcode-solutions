class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1] * len(nums)
        back = [i for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = max(dp[i], dp[j] + 1)
                        back[i] = j  
        print(dp)
        print(back)
        ans = []
        req_ind = dp.index(max(dp))
        # print(req_ind)
        ans.append(nums[req_ind])
        next = back[req_ind]
        while req_ind != next:
            # print(req_ind, next)
            ans.append(nums[next])
            req_ind = back[req_ind]
            next = back[req_ind]
        return ans