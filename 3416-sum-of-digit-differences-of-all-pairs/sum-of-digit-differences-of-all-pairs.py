class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        hashmap = defaultdict(dict)
        n = len(nums)
        # print(n)
        for i in range(len(nums)):
            for j in range(len(str(nums[i]))):
                if j not in hashmap[int(str(nums[i])[j])]:
                    hashmap[int(str(nums[i])[j])][j] = 0
                hashmap[int(str(nums[i])[j])][j] += 1
        
        ans = 0
        # print(hashmap)
        for i in range(len(nums)):
            for j in range(len(str(nums[i]))):
                # print(nums[i], str(nums[i])[j], j, hashmap[int(str(nums[i])[j])][j])
                # print(n - hashmap[int(str(nums[i])[j])][j])
                ans += (n - hashmap[int(str(nums[i])[j])][j])
        return ans // 2