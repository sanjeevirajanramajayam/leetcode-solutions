class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            temp = ""
            for j in range(i, len(s)):
                temp += s[j]
                if temp == temp[::-1]:
                    if len(temp) > len(ans):
                        ans = temp
        return ans