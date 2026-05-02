class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        hashset = set(nums)
        ans = float('-inf')
        for i in hashset:
            if i - 1 not in hashset:
                curr = i
                cnt = 0
                while curr in hashset:
                    cnt += 1
                    curr += 1
                ans = max(ans, cnt)
        return ans