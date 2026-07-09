class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        maxLen = float('-inf')
        for i in hashmap:
            if i + 1 in hashmap:
                maxLen = max(maxLen, hashmap[i] + hashmap[i + 1])
            # else:
                # maxLen = max(maxLen, hashmap[i])
        if maxLen == float('-inf'):
            return 0
        return maxLen