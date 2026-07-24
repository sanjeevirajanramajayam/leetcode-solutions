class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hash = {}
        k = len(p)
        p = Counter(p)
        if len(s) < k:
            return []
        for i in range(k):
            hash[s[i]] = hash.get(s[i], 0) + 1
        ans = []
        if hash == p:
            ans.append(0)
        # print(hash)
        for i in range(k, len(s)):
            # if s[i - k] in 'aeiou':
            hash[s[i - k]] = hash.get(s[i - k], 0) - 1
            if hash[s[i - k]] == 0:
                del hash[s[i - k]]
            # if s[i] in 'aeiou':
            hash[s[i]] = hash.get(s[i], 0) + 1
            # print(hash)
            if hash  == p :
                ans.append(i - k + 1)     
        return ans