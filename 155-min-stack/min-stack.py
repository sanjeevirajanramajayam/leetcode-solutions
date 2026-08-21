class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.stack:
            self.min = value
            self.stack.append(value)
        else:
            if value < self.min:
                self.stack.append(2 * value - self.min) 
                self.min = value
            else:
                self.stack.append(value)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] < self.min:
            self.min = - (self.stack[-1] - 2*self.min)
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack[-1] < self.min:
            return self.min
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()