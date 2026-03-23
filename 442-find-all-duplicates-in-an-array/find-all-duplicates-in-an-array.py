class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        ans = []
        for i in hashmap:
            if hashmap[i] == 2:
                ans.append(i)
        return ans