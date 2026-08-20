class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freqMap = Counter(power)
        keys = sorted(list(freqMap.keys()))
        @cache
        def fn(idx):
            print(idx)
            if idx >= len(keys):
                return 0
            take = float('-inf')
            i = idx
            while i < len(keys) and keys[i] <= keys[idx] + 2:
                i += 1
            # print("i =", i)
            take = (keys[idx] * freqMap[keys[idx]]) + fn(i)
            not_take = fn(idx + 1)

            return max(take , not_take)
        return fn(0)