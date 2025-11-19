class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        if k == len(num):
            return "0"

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # create string
        s = "".join(stack)

        # remove leading zeros
        news = ""
        for ch in s:
            if ch == "0" and news == "":
                continue
            news += ch

        # if everything removed
        if news == "":
            news = "0"

        # if k is still left, remove from end
        if k > 0:
            news = news[:-k] if k < len(news) else "0"

        return news
