class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        ans = [[boxGrid[j][i] for j in range(m)] for i in range(n)]
        for j in range(len(ans)):
            ans[j].reverse()
        # print(ans)
        for i in range(m):
            l = n - 1
            # print(m, n)
            while l >= 0 and ans[l][i] != '.':
                l -= 1
            r = l - 1
            # print(l, r)
            while r >= 0:
                # print(l, r)
                if ans[r][i] == '*':
                    r -= 1
                    l = r
                    continue
                if ans[r][i] == '#':
                    temp = ans[r][i]
                    ans[r][i] = ans[l][i]
                    ans[l][i] = temp
                    l -= 1
                r -= 1
        return ans