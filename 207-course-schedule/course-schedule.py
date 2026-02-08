class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjList = [[] for i in range(numCourses)]

        for startNode, endNode in (prerequisites):
            adjList[startNode].append(endNode)
        
        visited = [0 for i in range(numCourses)] 
        pathAlong = [0 for i in range(numCourses)] 

        def dfs(node):
            visited[node] = 1
            pathAlong[node] = 1
            for i in adjList[node]:
                if not visited[i]:
                    if not dfs(i):
                        return False
                if pathAlong[i] == 1:
                    return False
            pathAlong[node] = 0
            return True
        
        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return False
        
        return True