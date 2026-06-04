class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        cnt = 0
        for j in range(num1, num2 + 1):
            string = str(j)
            for i in range(len(string) - 3, -1, -1):
                # print(i, i + 1, i + 2, len(string))
                if (int(string[i + 1]) > int(string[i]) and int(string[i + 1]) > int(string[i + 2])) or (int(string[i + 1]) < int(string[i]) and int(string[i + 1]) < int(string[i + 2])):
                    cnt += 1
        return cnt