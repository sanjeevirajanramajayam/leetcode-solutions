class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for k in range(len(nums) - 1, -1, -1):
            i = 0
            j = k - 1

            while i < j:
                if nums[j] + nums[i] > nums[k]:
                    j -= 1
                    # print(i, j, k)
                    ans += (j - i + 1)
                else:
                    i += 1
        return ans
            