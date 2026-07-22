class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inorder = [0] * (n + 1)
        outorder = [0] * (n + 1)
        # adjList = [[] for i in range(n)]

        if n == 1 and trust == []:
            return n

        for s, e in trust: 
            inorder[e] += 1
            outorder[s] += 1
        # print(inorder)
        for i in range(n + 1):
            if inorder[i] == n - 1 and outorder[i] == 0:
                return i 
        return -1