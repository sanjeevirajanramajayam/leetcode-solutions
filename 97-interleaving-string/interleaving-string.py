class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def fn(i, j, k):
            if k < 0:
                if i < 0 and j < 0:
                    return True
                else:
                    return False
            if i < 0 and j < 0:
                return False
            ans = False
            if i >= 0 and s1[i] == s3[k]:
                ans = ans or fn(i - 1, j, k - 1)
            
            if j >= 0 and s2[j] == s3[k]:
                ans = ans or fn(i, j - 1, k - 1)
            
            return ans
        return fn(len(s1) - 1, len(s2) - 1, len(s3) - 1)