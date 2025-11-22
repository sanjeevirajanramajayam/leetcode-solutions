class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                element = stack.pop()
                if not stack:
                    pse = -1
                else:
                    pse = stack[-1]
                nse = i
                maxArea = max(maxArea, (nse - pse - 1) * heights[element])
            stack.append(i)
        while stack:
            element = stack.pop()
            if not stack:
                pse = -1
            else:
                pse = stack[-1]
            nse = len(heights)
            maxArea = max(maxArea, (nse - pse - 1) * heights[element])
        return maxArea