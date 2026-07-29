class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Len = len(s1)
        if len(s1) > len(s2):
            return False
        s1 = Counter(s1)
        dic = {}
        for i in range(0, s1Len):
            dic[s2[i]] = dic.get(s2[i], 0) + 1
        if dic == s1:
            return True
        for i in range(s1Len, len(s2)):
            dic[s2[i - s1Len]] -= 1
            if dic[s2[i - s1Len]] == 0:
                del dic[s2[i - s1Len]]
            dic[s2[i]] = dic.get(s2[i], 0) + 1
            if dic == s1:
                return True
        return False