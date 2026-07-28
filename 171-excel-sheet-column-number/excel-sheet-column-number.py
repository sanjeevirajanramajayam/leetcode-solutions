class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        mul = 1
        val = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            val += (ord(columnTitle[i]) - 65 + 1) * mul
            mul *= 26 
        return val