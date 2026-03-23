class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hashmap = {}
        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1
        # print(hashmap.values())
        if len(set(hashmap.values())) == 1:
            return True
        return False