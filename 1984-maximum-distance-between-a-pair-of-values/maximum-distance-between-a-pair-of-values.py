class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        ans = 0
        while j < len(nums2) and i < len(nums1):
            while nums2[j] >= nums1[i]:
                ans = max(ans, j - i)
                j += 1
                if j >= len(nums2):
                    break
                # print( j, i , j- i)

            i += 1
            # print("not eq", j, i)
        return ans