class Solution:
    def reverse(self, x: int) -> int:
        isNeg = False

        if x < 0:
            isNeg = True
            x = -x
        res = 0

        while x > 0:
            res = (res * 10) + x % 10  
            x //= 10

        if res > 2**31 - 1 or res < -2 ** 31:
            return 0
        if isNeg:
            res = -res
        return res