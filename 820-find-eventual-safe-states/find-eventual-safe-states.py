class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """

        res = []
        graph_new = [[] for i in range(len(graph))]
        inDegree = [0 for i in range(len(graph))]

        for i in range(len(graph)):
            for j in graph[i]:
                graph_new[j].append(i)
                inDegree[i] += 1
        
        queue = deque([])
        
        for i in range(len(graph)):
            if inDegree[i] == 0:
                queue.append(i)

        topo_sort = []
        
        while queue:
            node = queue.popleft()
            topo_sort.append(node)
            for i in graph_new[node]:
                inDegree[i] -= 1
                if inDegree[i] == 0:
                    queue.append(i)

        return sorted(topo_sort)