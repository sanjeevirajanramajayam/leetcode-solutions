class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)

        queue = deque([(beginWord, 1)])

        while queue:
            word, count = queue.popleft()
            if word == endWord:
                return count
            word = list(word)
            for i in range(len(word)):
                origChar = word[i]
                for ch in string.ascii_lowercase:
                    word[i] = ch
                    if "".join(word) in wordList:
                        wordList.remove("".join(word))
                        queue.append(("".join(word), count + 1))
                word[i] = origChar
        return 0
                     