class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2 = set(nums2)
        ans = []
        for i in set(nums1):
            if i in nums2:
                ans.append(i)
        return ans