class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        freqMap = {}
        for i in range(len(nums)):
            freqMap[nums[i]] = freqMap.get(nums[i], 0) + 1
        ans = []
        def fn(mapd, arr):
            if len(arr) == len(nums):
                ans.append(arr[:])
                return 
        
            for i in mapd:
                if mapd[i] != 0:
                    mapd[i] = mapd.get(i, 0) - 1
                    arr.append(i)
                    fn(mapd, arr)
                    mapd[i] = mapd.get(i, 0) + 1
                    arr.pop()
        fn(freqMap, [])
        return ans