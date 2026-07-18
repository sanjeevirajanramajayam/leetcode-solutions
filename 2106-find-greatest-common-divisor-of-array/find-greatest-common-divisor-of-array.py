class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # return math.gcd(max(nums), min(nums))
        def fn(a, b):
            if b == 0:
                return a
            return fn(b, a % b)
        
        return fn(max(nums), min(nums))