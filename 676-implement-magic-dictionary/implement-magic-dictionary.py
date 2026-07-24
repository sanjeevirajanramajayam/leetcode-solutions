class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()
    
    def insert_word(self, word):
        curr = self.root
        for ch in word:
            if curr.children[ord(ch) - ord('a')] is None: 
                curr.children[ord(ch) - ord('a')] = TrieNode()
            curr = curr.children[ord(ch) - ord('a')]
        curr.isEnd = True

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.insert_word(word)
        

    def search(self, searchWord: str) -> bool:
        def dfs(i, node, used):
            print(i, node, used)
            if i == len(searchWord):
                return node.isEnd and used
            # skip
            if not used:
                for j in range(len(node.children)):
                    if ord('a') + j == ord(searchWord[i]):
                        continue
                    if node.children[j] is not None:
                        if dfs(i + 1, node.children[j], True):
                            return True
            # go
            for j in range(26):
                if chr(ord('a') + j) == searchWord[i] and node.children[j] is not None:
                    if dfs(i + 1, node.children[j], used):
                        return True

            return False
        
        return dfs(0, self.root, False)

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)