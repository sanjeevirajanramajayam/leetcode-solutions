class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                hash = set()
                for k in range(j + 1, len(nums)):
                    if -(nums[i] + nums[j] + nums[k]) + target in hash:
                        temp = [nums[i], nums[j], nums[k], -(nums[i] + nums[j] + nums[k]) + target]
                        temp.sort()
                        ans.add(tuple(temp))
                    else:
                        hash.add(nums[k])
        
        return list(ans)