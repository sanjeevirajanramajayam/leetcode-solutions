class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        for x in range(len(edges)):
            edges[x].append(succProb[x])
        adjList = [[] for i in range(n)]
        for startNode, endNode, prob in edges:
            adjList[startNode].append((prob, endNode))
            adjList[endNode].append((prob, startNode))

        # print(edges)
        dist = [float('-inf')] * n
        dist[start_node] = 1
        pq = [(-1,start_node)]
        while pq:
            prob, node = heapq.heappop(pq)
            prob = -prob
            if prob < dist[node]:
                continue
            for newProb, endNode in adjList[node]:
                
                if prob * newProb > dist[endNode]:
                    dist[endNode] = prob * newProb
                    heapq.heappush(pq, (-(prob * newProb), endNode))
        if dist[end_node] == float('-inf'):
            return 0
        return dist[end_node]