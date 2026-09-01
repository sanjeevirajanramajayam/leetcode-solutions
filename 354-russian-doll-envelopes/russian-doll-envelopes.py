class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        ans = []

        def lower_bound(height):
            low = 0
            high = len(ans) - 1

            while low <= high:
                mid = (low + high) // 2

                if ans[mid] >= height:
                    high = mid - 1
                else:
                    low = mid + 1

            return low

        for width, height in envelopes:

            lb = lower_bound(height)

            if lb == len(ans):
                ans.append(height)
            else:
                ans[lb] = height

        return len(ans)