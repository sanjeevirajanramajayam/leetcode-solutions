class StockSpanner(object):

    def __init__(self):
        self.stack = []
        self.index = 0
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        ans = 1
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()
        if self.stack:
            ans = self.index - self.stack[-1][1]
        else:
            ans = self.index + 1
        self.stack.append((price, self.index))
        self.index += 1
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)