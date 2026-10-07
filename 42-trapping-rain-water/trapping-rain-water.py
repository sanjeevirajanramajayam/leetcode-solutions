class Solution:
    def trap(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        ans = 0
        leftMax = 0
        rightMax = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] < leftMax:
                    ans += leftMax - height[l]
                else:
                    leftMax = height[l]
                l += 1
            else:
                if height[r] < rightMax:
                    ans += rightMax - height[r]
                else:
                    rightMax = height[r]
                r -= 1
        return ans