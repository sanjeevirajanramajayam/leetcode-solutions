class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        evenCount = 0
        oddCount = 0
        ans = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] % 2 == 0:
                ans[i] = oddCount
                evenCount += 1
            else:
                ans[i] = evenCount
                oddCount += 1
            # print(oddCount, evenCount, ans)
        return ans