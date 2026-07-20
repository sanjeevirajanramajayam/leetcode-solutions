class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:
        adjList = [[] for i in range(n)]
        inorder = [0] * n
        for s, e in p:
            adjList[e].append(s)
            inorder[s] += 1

        queue = deque()
        
        for i in range(len(inorder)):
            if inorder[i] == 0:
                queue.append(i)
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            for i in adjList[node]:
                inorder[i] -= 1
                if inorder[i] == 0:
                    queue.append(i)
        if len(ans) != n:
            return []
        return ans