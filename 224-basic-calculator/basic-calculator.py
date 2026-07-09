class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        sign = 1
        currentNum = 0
        for ch in s:
            if ch == ' ':
                continue
            if ch.isdigit():
                currentNum = currentNum * 10 + int(ch)
                continue
            if ch == '+':
                result += currentNum * sign
                sign = 1
            elif ch == '-':
                result += currentNum * sign
                sign = -1
            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            else:
                # print(ch)
                result += currentNum * sign
                result *= stack.pop()
                result += stack.pop()
            currentNum = 0
        result += currentNum * sign
        return result

