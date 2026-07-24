class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 = Counter(s1)
        # s2 = {}
        s1h = Counter(s1)
        s2h = {}
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            s2h[s2[i]] = s2h.get(s2[i], 0) + 1
        if s2h == s1h:
            return True
        for i in range(len(s1), len(s2)):
            s2h[s2[i - len(s1)]] -= 1
            if s2h[s2[i - len(s1)]] == 0:
                del s2h[s2[i-len(s1)]]
            s2h[s2[i]] = s2h.get(s2[i], 0) + 1
            # print(s2h)
            if s2h == s1h:
                return True
        return False

