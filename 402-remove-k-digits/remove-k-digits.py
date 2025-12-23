class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == len(num):
            return "0"
        stack = []
        for i in range(len(num)):
            while stack and stack[-1] > num[i] and k > 0:
                k -= 1
                stack.pop()
            stack.append(num[i])

        s = "".join(stack)

        news = ""
        isNum = False

        for i in range(len(s)):
            if s[i] != "0":
                isNum = True
            if isNum:
                news += s[i]

        if k > 0:
            news = news[:len(news) - k]
        
        if news == "":
            return "0"
        return news