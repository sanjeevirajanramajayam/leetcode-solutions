class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert_word(self, word):
        curr = self.root

        for ch in word:
            idx = ord(ch) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()
        ans = set()

        trie = Trie()
        root = trie.root

        for word in words:
            trie.insert_word(word)
        
        def dfs(i, j, word, node):
            if not(i >= 0 and i < ROWS and j >= 0 and j < COLS and (i, j) not in visit and node.children[ord(board[i][j]) - ord('a')] != None):
                return
            
            word += board[i][j]
            node = node.children[ord(board[i][j]) - ord('a')]
            if node.is_end:
                ans.add(word)
            visit.add((i, j))
            dfs(i + 1, j, word, node)
            dfs(i, j + 1, word, node)
            dfs(i - 1, j, word, node)
            dfs(i, j - 1, word, node)
            visit.remove((i ,j))

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, "", root)

        return list(ans)