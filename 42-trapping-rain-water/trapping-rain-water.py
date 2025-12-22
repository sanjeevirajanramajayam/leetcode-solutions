class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        prefixList = [0]
        prefixMax = 0

        for i in range(1, len(height)):
            prefixMax = max(prefixMax, height[i - 1])
            prefixList.append(prefixMax)

        suffixList = [0] * len(height)
        suffixMax = 0

        for i in range(len(height) - 2, -1, -1):
            suffixMax = max(suffixMax, height[i + 1])
            suffixList[i] = (suffixMax)
        trapped = 0
        for i in range(len(height)):
            if height[i] < suffixList[i] and height[i] < prefixList[i]:
                trapped += min(suffixList[i], prefixList[i]) - height[i]
        return trapped