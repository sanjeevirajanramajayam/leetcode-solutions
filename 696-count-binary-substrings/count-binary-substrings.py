class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        current = s[0]
        strk = 0
        ans = 0
        for i in s:
            # print(i, current)
            if current == i:
                strk += 1
            else:
                groups.append(strk)
                strk = 1
                current = i
        groups.append(strk)
        
        for i in range(len(groups) - 1):
            ans += min(groups[i], groups[i + 1])
        
        return ans
            
