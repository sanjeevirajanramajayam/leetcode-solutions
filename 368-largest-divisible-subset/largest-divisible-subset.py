class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        dp = [1 for i in range(len(nums))]
        back = [i for i in range(len(nums))]
        for i in range(0, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = max(dp[i], dp[j] + 1)
                        back[i ] = j 
        maxi = float('-inf')
        for index, i in enumerate(dp):
            if i >= maxi:
                maxi = max(maxi, i)
                idx = index
        print(idx)
        curr = idx
        left = curr
        ans = []
        ans.append(nums[curr])
        print(ans)
        print(left, back[left])
        while left != back[left]:
            print(left, back[left])
            left = back[left]
            ans.append(nums[left])

        print(dp)
        print(back)
        return ans
        