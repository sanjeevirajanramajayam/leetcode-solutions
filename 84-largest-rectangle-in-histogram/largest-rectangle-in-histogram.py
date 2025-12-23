class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        def pse(arr):
            stack = []
            ans = [0] * len(heights)
            for i in range(len(heights)):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if not stack:
                    ans[i] = -1
                else:
                    ans[i] = stack[-1]
                stack.append(i)
            return ans

        def nse(arr):
            stack = []
            ans = [0] * len(heights)
            for i in range(len(heights) - 1, -1, -1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if not stack:
                    ans[i] = len(heights)
                else:
                    ans[i] = stack[-1]
                stack.append(i)
            return ans

        nse = nse(heights)
        pse = pse(heights)
        maxArea = 0

        for i in range(len(heights)):
            width = nse[i] - pse[i] - 1
            maxArea = max(width * heights[i], maxArea)
        
        return maxArea