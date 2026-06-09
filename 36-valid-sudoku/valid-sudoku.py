class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = {}
        colHash = {}
        squares = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if i in rowHash:
                    if board[i][j] in rowHash[i]:
                        return False
                else:
                    rowHash[i] = set()

                rowHash[i].add(board[i][j])

                if j in colHash:
                    if board[i][j] in colHash[j]:
                        return False
                else:
                    colHash[j] = set()

                colHash[j].add(board[i][j])
                
                if (i // 3, j // 3) in squares:
                    if board[i][j] in squares[(i // 3, j // 3)]:
                        return False
                else:
                    squares[(i // 3, j // 3)] = set()
                
                squares[(i // 3, j // 3)].add(board[i][j])
        return True