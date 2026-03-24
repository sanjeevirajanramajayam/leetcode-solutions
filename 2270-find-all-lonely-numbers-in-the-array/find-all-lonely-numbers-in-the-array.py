class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = hash.get(nums[i], 0) + 1
        ans = []
        for num in hash:
            if num - 1 not in hash and num + 1 not in hash and hash[num] == 1:
                ans.append(num)            
        return ans