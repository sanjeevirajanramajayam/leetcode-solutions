class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if curr.children[ord(ch) - ord('a')] is None:
                curr.children[ord(ch) - ord('a')] = TrieNode()
            curr = curr.children[ord(ch) - ord('a')]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(ind, node):
            # print(ind, node)
            if ind == len(word):
                if node.isEnd:
                    return True
                else:
                    return False
            
            ch = word[ind]
            if ch == '.':
                for ch in range(len(node.children)):
                    if node.children[ch] is not None:
                        if dfs(ind + 1, node.children[ch]):
                            return True
                return False
            else:
                if node.children[ord(ch) - ord('a')] is None:
                    return False
                else:
                    if dfs(ind + 1, node.children[ord(ch) - ord('a')]):
                        return True
            return False
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)