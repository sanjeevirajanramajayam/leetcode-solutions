class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        queue = deque([(beginWord, 1)])
        wordList = set(wordList)

        while queue:
            word, idx = queue.popleft()
            if word == endWord:
                return idx
            word = list(word)
            for i in range(0, len(word)):
                origChar = word[i]
                for ch in range(0, 27):
                    word[i] = chr(97 + ch)
                    if "".join(word) in wordList:
                        queue.append(("".join(word), idx + 1)) 
                        wordList.remove("".join(word))
                word[i] = origChar
        return 0
                    