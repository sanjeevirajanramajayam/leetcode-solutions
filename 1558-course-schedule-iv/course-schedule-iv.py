class Solution:
    def checkIfPrerequisite(self, n: int, p: List[List[int]], q: List[List[int]]) -> List[bool]:
        adjList = [[] for i in range(n)]
        inorder = [0 for i in range(n)]
        for s, e in p:
            adjList[s].append(e)
            inorder[e] += 1
        ancestor = [set() for i in range(n)]
        queue = deque([])
        for i in range(n):
            if inorder[i] == 0:
                queue.append((i, -1))
        while queue:
            node, anc = queue.popleft()
                # print(ancestor[node])
            for i in adjList[node]:
                inorder[i] -= 1
                ancestor[i].update(set([node]))
                ancestor[i].update(set(ancestor[node]))
                if inorder[i] == 0:
                    queue.append((i, node))
        # print(ancestor)
        ans = []
        for s, e in q:
            if s in ancestor[e]:
                ans.append(True)
            else:
                ans.append(False)
        return ans