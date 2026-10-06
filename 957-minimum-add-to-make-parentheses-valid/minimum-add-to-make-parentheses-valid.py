class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt = 0
        ans = 0
        for i in s:
            if i == "(":
                cnt += 1
            else:
                if cnt - 1 < 0:
                    ans += 1
                else:
                    cnt -= 1
            # print(cnt)
        return cnt + ans