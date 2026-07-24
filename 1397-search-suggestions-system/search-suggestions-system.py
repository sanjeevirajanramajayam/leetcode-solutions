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
    
    def search(self, prefix):
        self.ans = []
        curr = self.root
        for ch in prefix:
            if not curr.children[ord(ch) - ord('a')]: 
                return self.ans
            curr = curr.children[ord(ch) - ord('a')]

    
        def dfs(node, prefix):
            if len(self.ans) >= 3:
                return
            if node.isEnd:
                self.ans.append(prefix)
            for ch in range(len(node.children)):
                if node.children[ch]:
                    dfs(node.children[ch], prefix + chr((ch) + ord('a')))
        
        dfs(curr, prefix)
        temp = self.ans[:3]
        self.ans = []
        return temp



class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for word in products:
            trie.insert_word(word)
        ans = []
        for i in range(len(searchWord)):
            # print(searchWord[:i+1])
            ans.append(trie.search(searchWord[:i+1]))
        # print(ans)
        return ans