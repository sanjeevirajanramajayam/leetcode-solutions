class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)
        count = 0
        gi = 0
        si = 0
        while gi < len(g):
            if si >= len(s):
                break
            
            if s[si] >= g[gi]:
                count += 1
                si += 1

            gi += 1
        return count