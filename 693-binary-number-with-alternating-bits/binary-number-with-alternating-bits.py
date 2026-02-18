class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 1:
            return True
        curNum = 1
        # while 
        flag = True
        found = False
        while curNum <= n:
            print(curNum)
            if flag == True:
                curNum *= 2
            else:
                curNum *= 2
                curNum += 1
            if curNum == n:
                found = True
            flag = not flag
        return found
