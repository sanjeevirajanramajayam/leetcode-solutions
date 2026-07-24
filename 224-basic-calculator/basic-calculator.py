class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        currentNum = 0
        result = 0
        s += '+'
        for i in s:
            if i.isdigit():
                currentNum = currentNum * 10 + int(i)
                continue
            if i == ' ':
                continue
            if i == '+':
                result += currentNum * sign
                sign = 1
            elif i == '-':
                result += currentNum * sign
                sign = -1
            elif i == '(':
                stack.append(result)
                stack.append(sign)
                # print(stack)
                sign = 1
                result = 0
            elif i == ')':
                result += currentNum * sign
                result *= stack.pop()
                result += (stack.pop())
                sign = 1
            currentNum = 0
        return result

            

            
