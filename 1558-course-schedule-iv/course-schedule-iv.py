class Solution:
    def checkIfPrerequisite(self, n: int, p: List[List[int]], q: List[List[int]]) -> List[bool]:
        queue = deque([])
        prereq = [set() for i in range(n)]
        adjList = [[] for i in range(n)]
        inorder = [0 for i in range(n)]
        
        for startNode, endNode in p:
            adjList[startNode].append(endNode)
            inorder[endNode ] += 1
            prereq[endNode].add(startNode)
        
        for i in range(n):
            if inorder[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for nnode in adjList[node]:
                for req in prereq[node]:
                    prereq[nnode].add(req)
                inorder[nnode] -= 1
                if inorder[nnode] == 0:
                    queue.append(nnode)
        # print(prereq)
        ans = []
        for startNode, endNode in q:
            ans.append(startNode in prereq[endNode])
        return ans