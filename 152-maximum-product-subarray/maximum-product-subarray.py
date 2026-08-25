class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefixProd = 1
        suffixProd = 1
        maxProd = float('-inf')
        for i in range(len(nums)):
            prefixProd *= nums[i]
            maxProd = max(maxProd, prefixProd)
            if prefixProd == 0:
                prefixProd = 1

        for i in range(len(nums) - 1, -1, -1):
            suffixProd *= nums[i]
            maxProd = max(maxProd, suffixProd)
            if suffixProd == 0:
                suffixProd = 1
        
        return maxProd