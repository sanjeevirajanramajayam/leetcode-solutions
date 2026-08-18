class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # heap = [()]
        adjList = [[] for i in range(n)]

        for i in range(len(edges)):
            edges[i].append(succProb[i])
        # print(edges)
        for startNode, endNode, prob in edges:
            adjList[startNode].append((endNode, prob))
            adjList[endNode].append((startNode, prob))
        
        heap = [(-1, start_node)]
        dist = [float('-inf') for i in range(n)]
        dist[start_node] = 1
        while heap:
            prob, node = heapq.heappop(heap)
            # prob = -prob
            if -prob < dist[node]:
                continue
            
            for nnode, nprob in adjList[node]:
                if dist[node] * nprob > dist[nnode]:
                    dist[nnode] = dist[node] * nprob
                    heapq.heappush(heap, (-dist[nnode], nnode))
        # print(dist)
        if dist[end_node] == float('-inf'):
            return 0

        return dist[end_node]
