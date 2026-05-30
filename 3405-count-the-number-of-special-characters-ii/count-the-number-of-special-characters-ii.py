class Solution:
    def numberOfSpecialChars(self, s: str) -> int:
        map = {}
        for i in range(len(s)):
            if s[i] in string.ascii_uppercase and s[i] not in map:
                map[s[i]] = i
            elif s[i] in string.ascii_lowercase:
                map[s[i]] = i
        # print(map)
        cnt = 0
        for i in map:
            if i in string.ascii_lowercase and i.upper() in map and map[i] < map[i.upper()]:
                cnt += 1
        return cnt