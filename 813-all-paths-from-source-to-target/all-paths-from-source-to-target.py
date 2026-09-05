class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visited = set()
        path = []
        ans = []
        def dfs(node):
            nonlocal ans
            # print(node, path)
            visited.add(node)
            path.append(node)
            if node == len(graph) - 1:
                ans.append(path[:])
                visited.remove(node)
                path.pop()
                return
            for nnode in graph[node]:
                dfs(nnode)
            path.pop()
            visited.remove(node)
        dfs(0)
        return ans