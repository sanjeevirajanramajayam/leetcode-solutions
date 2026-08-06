class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash = {}
        cnt = 0
        for i in t:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        minLen = float('inf')
        l = 0
        r = 0
        startInd = -1
        while r < len(s):
            if hash.get(s[r], 0) > 0:
                cnt += 1
            hash[s[r]] = hash.get(s[r], 0) - 1

            while cnt == len(t):
                length = r - l + 1
                if length < minLen:
                    startInd = l
                minLen = min(minLen, length)

                hash[s[l]] += 1
                if hash[s[l]] > 0:
                    cnt -= 1
                
                l += 1
            
            r += 1
        if startInd == -1:
            return ""
        return s[startInd:startInd + minLen]