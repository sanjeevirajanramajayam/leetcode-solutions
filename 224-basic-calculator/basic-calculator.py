class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        currentNum = 0
        stack = []
        sign = 1
        for i in s:
            if i == " ":
                continue

            if i.isdigit():
                currentNum = currentNum * 10 + int(i)
                continue

            if i == "+":
                result += currentNum * sign
                sign = 1
            elif i == "-":
                result += currentNum * sign
                sign = -1
            elif i == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif i == ")":
                result += currentNum * sign
                result *= stack.pop()
                result += stack.pop()
                # result 
                sign = 1
            # print(result, i, sign, currentNum)
            currentNum = 0
        # if sign == 1:
        # print(currentNum, result)
        result += currentNum * sign

        return result 