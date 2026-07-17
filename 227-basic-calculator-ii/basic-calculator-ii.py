class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        currentNum = 0
        sign = '+'
        s += '+'
        for i in s:
            if i == ' ':
                continue
            if i.isdigit():
                currentNum = currentNum * 10 + int(i)
                continue
            if sign in '+-/*':
                # print(stack, i, sign, currentNum)
                # operand2 = stack.pop()
                # operand1 = stack.pop()
                if sign == '+':
                    # stack.push()
                    stack.append(currentNum)
                    sign = '+'
                elif sign == '-':
                    stack.append(-currentNum)
                    sign = '-'
                elif sign == '/':
                    stack.append(int(stack.pop() / currentNum))
                elif sign == '*':
                    stack.append(stack.pop() * currentNum)

            sign = i
            # stack.append(currentNum)
            currentNum = 0
        return sum(stack)