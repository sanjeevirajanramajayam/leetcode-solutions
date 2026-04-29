class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # left scan 
        ans = float('-inf')
        i = 0
        for j in range(len(colors) - 1, -1, -1):
            if colors[i] != colors[j]:
                ans = max(ans, abs(j - i))
        i = len(colors) - 1
        for j in range(0, len(colors) - 1):
            if colors[i] != colors[j]:
                ans = max(ans, abs(i - j))
        return ans