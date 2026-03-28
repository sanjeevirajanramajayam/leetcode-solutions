class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        min_num1 = min(nums1)
        min_num2 = min(nums2)

        nums1_set = set(nums1)
        nums2_set = set(nums2)

        common_set = nums1_set.intersection(nums2)
        ans = float('inf')
        if min_num1 == min_num2:
            ans = min(min_num1, ans)
        elif min_num1 < min_num2:
            ans = min(min_num1 * 10 + min_num2, ans)
        else:
            ans = min(min_num2 * 10 + min_num1, ans)
        
        min_commonality = float('inf') if common_set == set() else min(common_set)
        
        ans = min(min_commonality, ans)

        return ans
