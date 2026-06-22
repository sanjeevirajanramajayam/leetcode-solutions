class MyCalendarTwo:

    def __init__(self):
        self.map = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> bool:
        self.map[startTime] += 1
        self.map[endTime] -= 1
        prefix = 0
        for i in sorted(self.map.keys()):
            prefix += self.map[i]
            if prefix == 3:
                self.map[startTime] -= 1
                self.map[endTime] += 1
                return False
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)