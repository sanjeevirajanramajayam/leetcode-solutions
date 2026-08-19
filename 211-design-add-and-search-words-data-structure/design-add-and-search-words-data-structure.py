class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26

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

    def search_word(self, word):
        def dfs(node, index):
            # print(index)
            # print(node, index)
            if index == len(word):
                return node.isEnd

            if word[index] == '.':
                for x in range(26):
                    if node.children[x]:
                        if dfs(node.children[x], index + 1) is True:
                            return True
                return False
            else:
                curr = node
                for idx in range(index, len(word)):
                    ch = word[idx]
                    if ch == '.':
                        return dfs(curr, idx)
                    elif curr.children[ord(ch) - ord('a')] is None:
                        return False
                    else:
                        curr = curr.children[ord(ch) - ord('a')]
                return curr.isEnd
        return dfs(self.root, 0)

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert_word(word)

    def search(self, word: str) -> bool:
        return self.trie.search_word(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)