class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freqMap = Counter(nums)
        keys = sorted(freqMap.keys())
        @cache
        def fn(i):
            if i >= len(keys):
                return 0

            take = freqMap[keys[i]] * keys[i] 

            if i + 1 < len(keys) and keys[i + 1] == keys[i] + 1:
                take += fn(i + 2)
            else:
                take += fn(i + 1)

            not_take = fn(i + 1)

            return max(take , not_take)
        return fn(0)