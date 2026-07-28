class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert_word(self, word):
        curr = self.root
        for ch in word:
            if curr.children[ord(ch) - ord('a')] is None: 
                curr.children[ord(ch) - ord('a')] = TrieNode()
            curr = curr.children[ord(ch) - ord('a')]
        curr.isEnd = True
    
    def search_word(self, prefix):
        curr = self.root

        for ch in prefix:
            if curr.children[ord(ch) - ord('a')] is None: 
                return []
            curr = curr.children[ord(ch) - ord('a')]

        ans = []

        def dfs(node, temp):
            nonlocal ans
            if len(ans) >= 3:
                return
            if node.isEnd:
                ans.append(temp)
            for ch in range(len(node.children)):
                if node.children[ch] is not None:
                    dfs(node.children[ch], temp + chr(ord('a') + ch))
        
        dfs(curr, prefix)
        return ans[:3]

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()
        
        for word in products:
            t.insert_word(word)
        
        ans = []
        for i in range(len(searchWord)):
            ans.append(t.search_word(searchWord[:i + 1]))
        return ans
        
        