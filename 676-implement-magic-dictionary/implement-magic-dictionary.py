class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            curr = self.root
            for ch in word:
                if curr.children[ord(ch) - ord('a')] is None: 
                    curr.children[ord(ch) - ord('a')] = TrieNode()
                curr = curr.children[ord(ch) - ord('a')]
            curr.isEnd = True

    def search(self, searchWord: str) -> bool:
        def dfs(ind, skipped, node):
            if ind == len(searchWord):
                if skipped and node.isEnd:
                    return True
                else:
                    return False
            
            if not skipped:
                for ch in range(len(node.children)):
                    if chr(ord('a') + ch) == searchWord[ind]:
                        continue
                    if node.children[ch] is not None:
                        if dfs(ind + 1, True, node.children[ch]):
                            return True
            
            for ch in range(len(node.children)):
                if node.children[ch] is not None and chr(ord('a') + ch) == searchWord[ind]:
                    if dfs(ind + 1, skipped, node.children[ch]):
                        return True
            return False
        return dfs(0, False, self.root)
        



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)