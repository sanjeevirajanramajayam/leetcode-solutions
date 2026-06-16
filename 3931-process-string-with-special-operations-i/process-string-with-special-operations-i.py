class Solution:
    def processStr(self, s: str) -> str:
        temp = []
        for char in s:
            if char in string.ascii_lowercase:
                temp.append(char)
            elif char == '*':
                if temp:
                    temp.pop()
            elif char == '#':
                temp = 2 * temp
            else:
                temp = temp[::-1]
        return "".join(temp)
            