class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')' : '(', '}':'{', ']':'['}
        for i in s:
            if i not in hashmap:
                stack.append(i)
            elif stack and hashmap[i] == stack[-1]:
                stack.pop()
            else:
                return False
            
        return len(stack) == 0