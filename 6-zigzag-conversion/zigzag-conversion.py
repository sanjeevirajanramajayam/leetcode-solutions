class Solution:
    def convert(self, s: str, numRows: int) -> str:
        mat = [[] for i in range((numRows))]
        i = 0
        n = len(s)
        r = 0
        c = 0

        while i < n:
            for down in range(numRows):
                if i < n:
                    mat[down].append(s[i])
                    i += 1

            for up in range(numRows - 2, 0, -1):
                if i < n:
                    mat[up].append(s[i])
                    i += 1
        ans = ""
        for x in mat:
            ans += "".join(x)
        return ans