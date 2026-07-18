class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n == 1:
            return s
        negOnes = n // 2 + n % 2
        negOnes -= 1
        ans = ((n // 2) * m) + s - negOnes
        if n % 2 != 0:
            return max(ans, ans + 1)
        return ans