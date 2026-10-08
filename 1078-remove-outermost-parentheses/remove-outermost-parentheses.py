class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        cnt = 0
        for i in s:
            if i == '(':
                if cnt != 0:
                    ans += i
                cnt += 1
            else:
                cnt -= 1
                if cnt != 0:
                    ans += i
        return ans