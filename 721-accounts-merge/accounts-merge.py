class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        class DSU:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.rank = [1 for i in range(n)]
            
            def find_parent(self, node):
                if self.parent[node] == node:
                    return node
                self.parent[node] = self.find_parent(self.parent[node])
                return self.parent[node]

            def union(self, x, y):
                uX = self.find_parent(y)
                uY = self.find_parent(x)
                # rank = self.rank
                if uX == uY:
                    return  
                
                if self.rank[uX] > self.rank[uY]:
                    self.parent[uY] = uX
                elif self.rank[uY] > self.rank[uX]:
                    self.parent[uX] = uY
                else:
                    self.rank[uY] += 1
                    self.parent[uX] = uY
        
        dsu = DSU(len(accounts))
        
        emailIndMap = {}

        for i in range(len(accounts)):
            emails = accounts[i][1:]
            for email in emails:
                if email not in emailIndMap:
                    emailIndMap[email] = i
                else:
                    dsu.union(emailIndMap[email], i)
        
        print(dsu.parent)
        indEmailMap = defaultdict(list)

        for i in range(len(accounts)):
            origInd = dsu.find_parent(i)
            for email in accounts[i][1:]:
                indEmailMap[origInd].append(email)
        
        print(indEmailMap)
        arr = []
        for ind in indEmailMap:
            newArr = [accounts[ind][0]] + sorted(list(set(indEmailMap[ind])))
            arr.append(newArr)
        return arr