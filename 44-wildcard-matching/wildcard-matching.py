class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[-1 for i in range(len(p))] for i in range(len(s))]
        def fn(ind1, ind2):
            if ind1 < 0 and ind2 < 0:
                return True
            
            if ind1 < 0 and ind2 >= 0:
                for i in range(ind2 + 1):
                    if p[i] != "*":
                        return False
                return True
            
            if ind2 < 0 and ind1 >= 0:
                return False

            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]

            if s[ind1] == p[ind2] or p[ind2] == '?':
                dp[ind1][ind2] = fn(ind1 - 1, ind2 - 1)
                return dp[ind1][ind2]
            
            if p[ind2] == "*":
                dp[ind1][ind2] = fn(ind1 - 1, ind2) or fn(ind1, ind2 - 1)
                return dp[ind1][ind2] 
            dp[ind1][ind2] = False
            return False
        return fn(len(s) - 1, len(p) - 1)
             