class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        def higher_bound(target):
            ans = -1
            low = 0
            high = len(citations)
            while low <= high:
                mid = (low + high) // 2
                if citations[mid] >= target:
                    # print(citations[])
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans
        # print(citations, higher_bound(1))
        ans = 0
        for i in range(1, max(citations) + 1):
            if len(citations) - higher_bound(i) >= i:
                ans = i
            else:
                break

        return ans