class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS = len(mat)
        COLS = len(mat[0])
        ans=[]
        def goDownDiag(row, col):
            nonlocal ans
            temp = []
            while 0 <= row < ROWS and 0 <= col < COLS:
                temp.append(mat[row][col])
                row += 1
                col -= 1
            ans.append(temp)
        for i in range(COLS):
            goDownDiag(0, i)
        for i in range(1, ROWS):
            goDownDiag(i, COLS - 1)
        
        for i in range(len(ans)):
            if i % 2 == 0:
                ans[i] = ans[i][::-1]
        newAns = []
        for i in ans:
            for k in i: 
                newAns.append(k)
        return newAns