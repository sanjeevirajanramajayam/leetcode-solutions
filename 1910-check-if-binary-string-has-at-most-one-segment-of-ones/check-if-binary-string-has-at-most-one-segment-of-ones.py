class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seenOneOnce = False
        inOne = False
        for i in s:
            if i == '0' and inOne:
                inOne = False
            if seenOneOnce == True and i == '1' and inOne == False:
                return False
            if i == '1':
                seenOneOnce = True
                inOne = True
        return True