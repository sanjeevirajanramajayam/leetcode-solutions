class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        print(hashmap)
        cnt = 0
        isOdd = False
        for i in hashmap:
            if hashmap[i] % 2 == 0:
                cnt += hashmap[i] 
            else:
                isOdd = True
                cnt += (hashmap[i] - 1)
        if isOdd:
            cnt += 1
        return cnt