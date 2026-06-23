class Solution:
    def numTrees(self, n: int) -> int:
        nodeSum = [0] * (n + 1)
        nodeSum[0] += 1
        nodeSum[1] += 1
        for node in range(2, n + 1):
            totalSum = 0
            for j in range(1, node + 1):
                totalSum += nodeSum[j - 1]  * nodeSum[node - j]
            nodeSum[node] = totalSum
        return nodeSum[n]