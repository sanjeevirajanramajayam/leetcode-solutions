class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = []
        for i in range(len(heights) - 1, -1, -1):
            visible = 0
            while stack and stack[-1] < heights[i]:
                visible +=1
                stack.pop()
            
            if stack:
                visible += 1

            ans.append(visible)
            stack.append(heights[i])

        return ans[::-1]
