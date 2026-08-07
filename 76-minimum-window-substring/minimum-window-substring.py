class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash = {}
        for i in t:
            hash[i] = hash.get(i, 0) + 1
        oldLen = len(hash)
        startChar = -1
        ans = float('inf')
        cnt = 0
        l = 0
        for r in range(len(s)):
            hash[s[r]] = hash.get(s[r], 0) - 1
            if hash[s[r]] == 0:
                cnt += 1
            # print(hash, cnt)
            while cnt == oldLen:
                if ans > r - l + 1:
                    ans = r- l + 1
                    startChar = l
                hash[s[l]] = hash.get(s[l], 0) + 1
                if hash[s[l]] > 0:
                    cnt -= 1
                l += 1
                # print(cnt, l, s[l:r+1])
        if startChar == -1:
            return ""
        return s[startChar:startChar+ans]
        print(startChar, ans)