class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = sorted(set(arr))
        hash = {}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = i + 1
        # print(nums)
        # print(hash)
        ans = []
        for i in range(len(arr)):
            ans.append(hash[arr[i]])
        return ans