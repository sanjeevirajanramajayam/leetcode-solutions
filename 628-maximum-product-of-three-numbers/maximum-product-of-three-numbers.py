class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        l1 = float('-inf')
        l2 = float('-inf')
        l3 = float('-inf')
        s1 = float('inf')
        s2 = float('inf')
        s3 = float('inf')

        for i in nums:
            if i > l1:
                l3 = l2 
                l2 = l1
                l1 = i 
            elif i > l2:
                l3 = l2
                l2 = i 
            elif i > l3:
                l3 = i 
            
            if s1 > i:
                s3 = s2 
                s2 = s1 
                s1 = i 
            elif s2 > i:
                s3 = s2 
                s2 = i 
            elif s3 > i:
                s3 = i
        # print(l1, l2, l3, s1, s2, s3)
        return max(l1 * l2 * l3, s1 * s2 * l1)