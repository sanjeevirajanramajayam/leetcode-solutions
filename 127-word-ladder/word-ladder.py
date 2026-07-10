class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([(beginWord, 1)])
        wordList = set(wordList)
        while queue:
            word, cnt = queue.popleft()
            if word == endWord:
                return cnt
            word = list(word)
            for i in range(len(word)):
                originalChar = word[i]
                for j in range(ord('a'), ord('z') + 1, 1):
                    word[i] = chr(j)
                    if "".join(word) in wordList:
                        wordList.remove("".join(word))
                        queue.append(("".join(word), cnt + 1))
                word[i] = originalChar
        return 0