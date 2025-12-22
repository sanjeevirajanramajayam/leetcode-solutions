class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = {}
        res = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            if not stack:
                ans[nums2[i]] = -1
            else:
                ans[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        for i in nums1:
            res.append(ans[i])
        return res