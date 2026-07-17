class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        for i in range(len(succProb)):
            edges[i].append(succProb[i])
        
        adjList = [[] for i in range(n)]

        for s, e, p in edges:
            adjList[s].append((e, p))
            adjList[e].append((s, p))
        
        pq = [(-1, start_node)]

        distArray = [float('-inf') for i in range(n)] 
        distArray[start_node] = 1
        while pq:
            prob, node = heapq.heappop(pq)            
            prob = -prob
            if prob > distArray[node]:
                continue
            if node == end_node:
                return prob
            # prob = -prob
            for nnode, p in adjList[node]:
                newProb = prob * p
                if newProb > distArray[nnode]:
                    distArray[nnode] = newProb
                    heapq.heappush(pq, (-distArray[nnode], nnode))
        print(distArray)
        return 0
