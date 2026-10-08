class RandomizedSet:

    def __init__(self):
        self.array = []
        self.set = {}

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set[val] = len(self.array)
        self.array.append(val)
        return True 

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False 
        lastI = self.set[self.array[-1]]
        valI = self.set[val]
        self.set[self.array[lastI]] = valI 

        self.array[valI], self.array[lastI] = self.array[lastI], self.array[valI]
        self.array.pop()
        del self.set[val]
        return True 

    def getRandom(self) -> int:
        return self.array[random.randint(0, len(self.array) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()