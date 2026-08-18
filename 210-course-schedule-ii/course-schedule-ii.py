class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:
        queue = deque([])
        adjList = [[] for i in range(n)]
        inorder = [0] * n
        for startNode, endNode in p:
            adjList[endNode].append(startNode)
            inorder[startNode] += 1
        # print(adjList, inorder)
        for i in range(n):
            if inorder[i] == 0:
                queue.append(i)
        # print(inorder)
        ans = []
        while queue:
            # print(queue, inorder)
            node = queue.popleft()
            ans.append(node)
            for nnode in adjList[node]:
                inorder[nnode] -= 1
                if inorder[nnode] == 0:
                    queue.append(nnode)
        if len(ans) != n:
            return []
        return ans
