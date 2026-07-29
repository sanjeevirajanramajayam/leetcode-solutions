class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        queue = deque([(1, beginWord)])

        while queue:
            cnt, word = queue.popleft()
            if word == endWord:
                return cnt
            word = list(word)
            for i in range(len(word)):
                orig = word[i]
                for ch in string.ascii_lowercase:
                    word[i] = ch
                    if "".join(word) in wordSet:
                        queue.append((cnt + 1, "".join(word)))
                        wordSet.remove("".join(word))
                word[i] = orig
        return 0