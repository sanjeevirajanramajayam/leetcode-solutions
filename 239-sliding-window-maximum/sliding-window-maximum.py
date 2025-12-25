class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [0] * (len(nums) - (k - 1))
        dq = deque()
        for i in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            while dq and dq[0] <= i - k:
                dq.popleft()
            dq.append(i)
            if i >= (k - 1):
                ans[i - (k - 1)] = nums[dq[0]]      
        return ans      