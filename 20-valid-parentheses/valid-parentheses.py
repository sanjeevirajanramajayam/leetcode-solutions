class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {')' : '(',
        ']':'[',
        '}':'{'}

        for i in range(len(s)):
            if s[i] in map:
                if stack and stack[-1] != map[s[i]]:
                    return False
                if stack:
                    stack.pop()
                else:
                    return False
                continue
            stack.append(s[i])
            # print(stack)
        return len(stack) == 0