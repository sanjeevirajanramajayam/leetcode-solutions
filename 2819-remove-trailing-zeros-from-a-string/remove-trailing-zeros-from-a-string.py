class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        nums = list(num)
        while nums and nums[-1] == '0':
            nums.pop()
        return "".join(nums)