class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hash = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] != nums[j]:
                    hash[nums[i] * nums[j]] = hash.get(nums[i] * nums[j], 0) + 1
                    # print(nums[i], nums[j], nums[i] * nums[j])
        # print(hash)
        cnt = 0
        for prod in hash:
            cnt += (hash[prod]) * (hash[prod] - 1)
        return cnt * 4