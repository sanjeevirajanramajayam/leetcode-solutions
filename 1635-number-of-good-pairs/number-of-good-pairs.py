class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash = {}
        count = 0
        for i in range(len(nums)):
            hash[nums[i]] = hash.get(nums[i], 0) + 1

        for i in hash:
            count += 1 if (hash[i] * (hash[i] - 1) / 2) == 1 else (hash[i] * (hash[i] - 1) / 2)
        
        return int(count)