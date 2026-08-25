class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.numMap = {}

    def insert(self, val: int) -> bool:
        res = False
        if val not in self.numMap:
            res = True
        if res:
            self.nums.append(val)
            self.numMap[val] = len(self.nums) -1
        return res
        

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            idx = self.numMap[val]
            lastVal = self.nums[-1]
            self.nums[idx] = lastVal
            self.nums.pop()
            self.numMap[lastVal] = idx
            del self.numMap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()