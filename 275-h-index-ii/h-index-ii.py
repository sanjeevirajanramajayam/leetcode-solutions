class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cnt = 0
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                # break
                return len(citations) - 1 - i + 1
            # cnt += 1

        # return cnt
        return 0