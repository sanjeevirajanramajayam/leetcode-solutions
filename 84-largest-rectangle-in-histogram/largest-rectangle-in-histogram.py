class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        stack = []
        ans = [0] * len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                nse = i
                element = stack.pop()
                if stack:
                    pse = stack[-1]
                else:
                    pse = -1
                width = nse - pse - 1
                maxArea = max(maxArea, width * heights[element])
            if not stack:
                ans[i] = -1
            else:
                ans[i] = stack[-1]
            stack.append(i)

        while stack:
            element = stack.pop()
            if stack:
                pse = stack[-1]
            else:
                pse = -1
            nse = len(heights)
            width = nse - pse - 1
            maxArea = max(maxArea, width * heights[element])
        return maxArea
