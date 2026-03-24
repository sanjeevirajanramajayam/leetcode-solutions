class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hash = {}
        for hour in hours:
            hash[hour % 24] = hash.get(hour % 24, 0) + 1
        # print(hash)
        pairs = 0
        for rem in hash:
            comp = (24 - rem) % 24
            if rem == 0:
                pairs += hash[rem] * (hash[rem] - 1) // 2
            elif rem == 12:
                pairs += hash[rem] * (hash[rem] - 1) // 2
            elif rem > comp:

                pairs += hash[rem] * hash.get(comp, 0)

        return pairs