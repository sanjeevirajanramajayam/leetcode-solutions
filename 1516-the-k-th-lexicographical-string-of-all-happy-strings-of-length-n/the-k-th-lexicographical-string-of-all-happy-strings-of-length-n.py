class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        chars = ['a', 'b', 'c']
        count = [0]
        def getAll(i, s, last):
            if i == n:
                res.append("".join(s[:]))
                count[0] += 1
                # print(count, s)
                if count[0] == k:
                    count[0] = "".join(s[:])
                    return True
                return False
            for char in chars:
                if char != last:
                    s.append(char)
                    if getAll(i + 1, s, char):
                        return True
                    s.pop()

        if getAll(0, [], "z"):
            return count[0]
        else:
            return ""