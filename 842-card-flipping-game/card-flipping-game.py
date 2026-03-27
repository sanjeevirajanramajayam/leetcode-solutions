class Solution:
    def flipgame(self, nums: List[int], backs: List[int]) -> int:
        candidates = set(nums)
        candidates.update(set(backs))
        # print(candidates)
        hash = {}

        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = set()

            hash[nums[i]].add(backs[i])
            if backs[i] not in hash:
                hash[backs[i]] = set()

            hash[backs[i]].add(nums[i])

        # print(hash)

        min_val = float('inf')
        # print(candidates)
        for i in candidates:
            if i not in hash[i]:
                # print(i)
                min_val = min(min_val, i)
        
        return 0 if min_val == float('inf') else min_val