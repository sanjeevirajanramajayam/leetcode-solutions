class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hash = {}
        for t in time:
            hash[t % 60] = hash.get(t % 60, 0) + 1

        count = 0
        print(hash)
        visited = set()
        for rem in hash:
            if rem in visited:
                continue
            if rem == 30 or rem == 0:
                count += hash[rem] * (hash[rem] - 1) // 2
            else:
                if (60 - rem) in hash:
                    count += hash[rem] * hash[60 - rem]
                    visited.add(60 - rem)
        return count
