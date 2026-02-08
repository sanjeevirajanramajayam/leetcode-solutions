class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adjList = [[] for i in range(numCourses)]
        inDegree = [0 for i in range(numCourses)] 

        for startNode, endNode in (prerequisites):
            adjList[endNode].append(startNode)
            inDegree[startNode] += 1
        
        topo_sort = []

        queue = deque([])

        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            topo_sort.append(node)
            for i in adjList[node]:
                inDegree[i] -= 1
                if inDegree[i] == 0:
                    queue.append(i)
        
        if len(topo_sort) != numCourses:
            return []
        
        return topo_sort

        
