class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = float('-inf')
        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i] != colors[j]:
                    ans = max(ans, abs(i - j))
        return ans