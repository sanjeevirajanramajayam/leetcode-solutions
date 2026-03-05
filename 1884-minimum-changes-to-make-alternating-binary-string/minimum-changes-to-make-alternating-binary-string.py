class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = 0
        op = 0
        news = s
        for i in news:
            flag = not flag
            if int(i) != flag:
                op += 1
        final_op = op
        flag = 1
        op = 0
        news = s

        for i in news:
            flag = not flag
            if int(i) != flag:
                op += 1
        final_op = min(final_op, op)
        return final_op