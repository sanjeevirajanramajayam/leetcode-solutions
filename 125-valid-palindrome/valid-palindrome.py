class Solution:
    def isPalindrome(self, s2: str) -> bool:
        s = ""
        for i in s2:
            if i.isalnum():
                s += i
        # print(s)
        return s.lower() == s.lower()[::-1]