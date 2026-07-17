class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:
        adjList = [[] for i in range(n)]
        inorder = [0] * n
        queue = deque([])
        for sn, en in p:
            adjList[en].append(sn)
            inorder[sn] += 1
        for i in range(len(adjList)):
            if inorder[i] == 0:
                queue.append(i)
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            for nn in adjList[node]:
                inorder[nn] -= 1
                if inorder[nn] == 0:
                    queue.append(nn)
        if len(ans) != n:
            return []
        return ans