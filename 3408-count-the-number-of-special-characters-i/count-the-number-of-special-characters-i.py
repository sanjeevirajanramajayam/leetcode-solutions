class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        uniq = set(list(word.lower()))
        cnt = 0
        for i in uniq:
            if i in word and i.upper() in word:
                cnt += 1
        return cnt