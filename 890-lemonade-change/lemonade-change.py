class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fiveCount = 0
        tenCount = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                fiveCount += 1
            
            if bills[i] == 10:
                if fiveCount == 0:
                    return False
                tenCount += 1
                fiveCount -= 1
            
            if bills[i] == 20:
                if tenCount >= 1 and fiveCount >= 1:
                    tenCount -= 1
                    fiveCount -= 1
                elif fiveCount >= 3:
                    fiveCount -= 3
                else:
                    return False
        return True