class Solution:
    def getHint(self, s: str, g: str) -> str:
        sh = Counter(s)
        gh = Counter(g)
        b = 0
        c = 0
        for i in range(len(s)):
            if s[i] == g[i]:
                sh[s[i]] -= 1
                b += 1
        for i in range(len(s)):
            if s[i] != g[i]:
                if sh[g[i]] != 0:
                    sh[g[i]] -= 1
                    c += 1
        return(f"{b}A{c}B")