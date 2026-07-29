class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic = {}
        lenP = len(p)
        if len(p) > len(s):
            return []
        for i in range(0, len(p)):
            dic[s[i]] = dic.get(s[i], 0) + 1
        p = Counter(p)
        ans = []
        if dic == p:
            ans.append(0)
        for i in range(lenP, len(s)):
            dic[s[i - lenP]] -= 1
            if dic[s[i - lenP]] == 0:
                del dic[s[i - lenP]] 
            dic[s[i]] = dic.get(s[i], 0) + 1
            if dic == p:
                ans.append(i - lenP + 1)
        return ans
