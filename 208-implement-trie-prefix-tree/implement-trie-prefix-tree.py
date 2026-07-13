class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            idx = ord(i) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.isEnd = True
        return curr

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            idx = ord(i) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return curr.isEnd == True
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            idx = ord(i) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)