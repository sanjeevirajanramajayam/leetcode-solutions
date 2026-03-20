class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [int(x) for x in list(str(int("".join([str(i) for i in num])) + k))]