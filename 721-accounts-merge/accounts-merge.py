class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailMap = {} # email - index

        class DSU:
            def __init__(self, V):
                self.V = V
                self.parent = [i for i in range(V)]
                self.rank = [0 for i in range(V)]
            
            def find_parent(self, node):
                if node == self.parent[node]:
                    return node
                self.parent[node] = self.find_parent(self.parent[node])
                return self.parent[node] 
            
            def union(self, u, v):
                uPar = self.find_parent(u)
                vPar = self.find_parent(v)

                if uPar == vPar:
                    return
                
                if self.rank[uPar] > self.rank[vPar]:
                    self.parent[vPar] = uPar 
                elif self.rank[vPar] > self.rank[uPar]:
                    self.parent[uPar] = vPar
                else:
                    self.parent[uPar] = vPar
                    self.rank[vPar] += 1

        dsu = DSU(len(accounts))
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email in emailMap:
                    dsu.union(i, emailMap[email])
                else:
                    emailMap[email] = i
        
        ans = [[] for _ in range(len(accounts))]

        for email, index in emailMap.items():
            newIndex = dsu.find_parent(index)
            if ans[newIndex] == []:
                ans[newIndex].append(accounts[newIndex][0])
            ans[newIndex].append(email)
        # print(ans)
        return [[x[0]] + sorted(x[1:]) for x in ans if x != []]