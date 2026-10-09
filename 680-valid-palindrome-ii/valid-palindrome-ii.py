class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalidrome(l, r):
            return s[l:r+1] == s[l:r+1][::-1]
        
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPalidrome(l + 1, r) or isPalidrome(l, r-1)
        return True