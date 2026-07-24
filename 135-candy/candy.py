class Solution:
    def candy(self, nums: List[int]) -> int:
        n = len(nums)
        candies = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                candies[i] = candies[i - 1] + 1
        # print(candies)
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                if candies[i] <= candies[i + 1]:
                    candies[i] = candies[i + 1] + 1
        # print(candies)
        return sum(candies)