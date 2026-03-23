class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)
        ans = [0, 0]
        for i in nums1:
            if i in nums2Set:
                ans[0] += 1
        
        
        for i in nums2:
            if i in nums1Set:
                ans[1] += 1
        
        return ans