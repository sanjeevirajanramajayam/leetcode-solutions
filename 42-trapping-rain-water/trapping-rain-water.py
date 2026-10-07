class Solution:
    def trap(self, height: list[int]) -> int:
        prefixMax = [0]
        suffixMax = [0] * len(height)

        for i in range(1, len(height)):
            prefixMax.append(max(prefixMax[-1], height[i - 1]))
        
        for i in range(len(height) - 2, -1, -1):
            suffixMax[i] = (max(suffixMax[i + 1], height[i + 1]))
        ans = 0
        for i in range(len(height)):

            if height[i] < prefixMax[i] and height[i] < suffixMax[i]:
                # print(i, height[i], prefixMax[i], suffixMax[i])
                ans += min(prefixMax[i], suffixMax[i]) - height[i]
                # print(ans)
        return ans