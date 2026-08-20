class Solution:
    def numDecodings(self, s: str) -> int:

        for i in range(len(s)):
            if s[i] == '0':
                if i - 1 >= 0:
                    if s[i - 1] not in ('1', '2'):
                        return 0
                else:
                    return 0
        @cache
        def fn(i):
            if i == len(s):
                return 1
            ans = 0
            for x in range(i, len(s)):
                if int(s[i:x+1]) <= 26:
                    # print(int(s[i:x+1]))
                    # print(s[x], x)
                    if int(s[i:x+1]) > 0 and s[i] != '0':
                        ans += fn(x+1)
            return ans
        return fn(0)  