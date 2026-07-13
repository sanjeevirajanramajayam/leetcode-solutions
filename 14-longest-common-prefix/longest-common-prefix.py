class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""
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

            def oneChild(self, root) -> bool:
                cnt = 0
                for i in root.children:
                    if i:
                        cnt += 1
                    if cnt > 1:
                        return False
                if cnt <= 0:
                    return False
                return True

            def startsWith(self):
                curr = self.root
                ans = ""
                # for i in prefix:
                while self.oneChild(curr) and not curr.isEnd:
                    # idx = ord(i) - ord('a')
                    for i in range(len(curr.children)):
                        if curr.children[i]:
                            idx = i
                            break
                    ans += chr(ord('a') + i)
                    if not curr.children[idx]:
                        return False
                    curr = curr.children[idx]
                    # else:
                        # break

                return ans

        t = Trie()
        for word in strs:
            t.insert(word)
        return t.startsWith()
