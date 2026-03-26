class Solution:
    def partitionString(self, s: str) -> int:
        hash = set()
        partition = 1
        for i in range(len(s)):
            # print(hash, s[i], partition)
            if s[i] in hash:
                hash = set()
                hash.add(s[i])
                partition += 1
            else:
                hash.add(s[i])
        return partition