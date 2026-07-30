class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[] for i in range(numRows)]
        # print(matrix)
        i = 0
        while i < len(s):
            for down in range(numRows):
                if i < len(s):
                    matrix[down].append(s[i])
                i += 1

            for up in range(numRows - 2, 0, -1):
                if i < len(s):
                    matrix[up].append(s[i])
                i += 1
        ans = ""
        for x in matrix:
            print(x)
            ans += "".join(x)
        return ans