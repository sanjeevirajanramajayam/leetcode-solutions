class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = float('-inf')
        prod = 1
        suffix = 1
        for i in range(len(nums)):
            prod *= nums[i]
            suffix *= nums[len(nums) - 1 - i]
            # print(prod, suffix)
            maxProd = max(maxProd, prod, suffix)

            if prod == 0:
                prod = 1
            
            if suffix == 0:
                suffix = 1
        return maxProd
