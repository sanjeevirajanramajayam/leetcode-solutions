class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxi = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    maxi = max(maxi, i - stack[-1])
                else:
                    stack.append(i)
            # print(stack)
        return maxi