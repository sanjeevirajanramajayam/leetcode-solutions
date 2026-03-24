class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        onearray = []
        MOD = 12345
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                onearray.append(grid[i][j] % MOD)
        
        prefixArray = [1]
        prod = 1
        for i in range(len(onearray)):
            prod *= onearray[i]
            prefixArray.append(prod % MOD)
        prod = 1
        suffixArray = [1 for i in range(len(onearray))]
        for i in range(len(onearray) - 1, -1, -1):
            prod *= onearray[i]
            suffixArray[i] = prod % 12345
        suffixArray.append(1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(i, j)
                # print(i * len(grid[0]) + j)
                grid[i][j] = (prefixArray[i * len(grid[0]) + j] * suffixArray[i * len(grid[0]) + j + 1]) % 12345
        
        return grid