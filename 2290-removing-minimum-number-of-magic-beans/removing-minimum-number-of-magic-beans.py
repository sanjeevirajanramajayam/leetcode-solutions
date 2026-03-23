class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans = sorted(beans)
        prefixSum = [0 for i in range(len(beans) + 1)]

        for i in range(len(beans)):
            prefixSum[i + 1] = prefixSum[i] + beans[i]
        minBeans = float('inf')
        for i in range(len(beans)):
            # print(beans[i] * (len(beans) - i - 1))
            # print((prefixSum[-1] - prefixSum[i + 1]))
            leftBeans = prefixSum[i]
            rightBeans = (prefixSum[-1] - prefixSum[i + 1]) - beans[i] * (len(beans) - i - 1)
            minBeans = min(leftBeans + rightBeans, minBeans)
            # print(rightBeans)
        return minBeans