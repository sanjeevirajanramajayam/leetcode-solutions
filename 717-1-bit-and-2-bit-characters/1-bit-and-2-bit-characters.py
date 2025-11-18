class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        jump = False
        for i in range(len(bits)):
            # print(i, bits[i], jump)
            if jump == True:
                jump = False
                continue
            if bits[i] == 1:
                jump = True
            if i == (len(bits) - 1) and bits[i] == 0:
                return True
        return False