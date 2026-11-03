class RandomizedSet:

    def __init__(self):
        self.array = []
        self.hashmap = {}

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.array)
            self.array.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            idx = self.hashmap[val]
            self.hashmap[self.array[len(self.array) - 1]] = idx
            self.array[idx], self.array[len(self.array) - 1] = self.array[len(self.array) - 1], self.array[idx]
            del self.hashmap[self.array[-1]]
            self.array.pop()
            
            # self.hashmap[val] = 
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.array[random.randint(0, len(self.array) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()