class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqMap = {}
        
        for i in t:
            freqMap[i] = freqMap.get(i, 0) + 1
        prevLen = len(freqMap)
        l = 0
        cnt = 0
        start = -1
        alen = float('inf')
        for r in range(len(s)):
            freqMap[s[r]] = freqMap.get(s[r], 0) - 1
            if freqMap[s[r]] == 0:
                cnt += 1
            # print(cnt, len(freqMap))
            while cnt >= prevLen:
                # print(s[l:r+1])
                if cnt == prevLen:
                    if alen > (r - l + 1):
                        alen = (r - l + 1)        
                        start = l
                freqMap[s[l]] += 1
                if freqMap[s[l]] > 0:
                    cnt -= 1
                l += 1
        # print(start, start + alen)
        if start == -1:
            return ""
        return s[start:start+alen]