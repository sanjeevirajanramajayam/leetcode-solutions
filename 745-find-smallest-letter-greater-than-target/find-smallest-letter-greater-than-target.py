class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        found = False
        compChar = '0'
        for i in letters:
            if found == False:
                # print(i, target, i < target)
                if i > target:
                    compChar = i
                    found = True
            else:
                if i < compChar:
                    compChar = i
        if compChar == '0':
            return letters[0]
        return compChar