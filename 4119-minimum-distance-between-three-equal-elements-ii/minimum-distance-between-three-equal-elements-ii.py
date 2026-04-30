class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        freqMap = defaultdict(list)
        for i in range(len(nums)):
            freqMap[nums[i]].append(i)
        val = float('inf')
        for key in freqMap:
            indList = freqMap[key]
            # print(indList)
            if len(indList) < 3:
                continue
            for i in range(0, len(indList) - 3 + 1):
                a = indList[i] 
                b = indList[i + 1]
                c = indList[i + 2]
                # print(indList, a, b , c)
                val = min(val, abs(a - b) + abs(b - c) + abs(c - a))
        if val == float('inf'):
            return -1
        return val
