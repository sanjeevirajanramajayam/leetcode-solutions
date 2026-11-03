class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        stack = deque([])
        ans = []
        for i in range(len(nums)):
            while stack and nums[i] >= nums[stack[-1]]:
                stack.pop()
            while stack and i - k >= stack[0]:
                stack.popleft()
            stack.append(i)
            if i - k + 1 >= 0:
                ans.append(nums[stack[0]])
            # print(stack)
        return ans
