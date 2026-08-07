class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {}
        l = 0
        maxFreq = float('-inf')
        maxChar = '-1' 
        ans = 0
        for r in range(len(s)):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1

            if freqMap[s[r]] > maxFreq:
                maxChar = s[r]
                maxFreq = freqMap[s[r]]

            while maxFreq + k < r - l + 1:
                freqMap[s[l]] -= 1
                if freqMap[s[l]] == 0:
                    del freqMap[s[l]]

                maxFreq = float('-inf')
                maxChar = '-1' 

                for key in freqMap:
                    if freqMap[key] > maxFreq:
                        maxChar = key
                        maxFreq = freqMap[key]
                
                l += 1
            
            ans = max(ans, r - l + 1)
        return ans