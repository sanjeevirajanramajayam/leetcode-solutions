class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        hash = {}
        for key, pair in knowledge:
            hash[key] = pair
        ans = ''
        r = 0
        while r < len(s):
            if s[r] == '(':
                temp = ''
                r += 1
                while s[r] != ')':
                    temp += s[r] 
                    r += 1
                if temp in hash:
                    ans += hash[temp]
                else:
                    ans += '?'
                r += 1
                continue
            ans += s[r]
            r += 1
        return ans