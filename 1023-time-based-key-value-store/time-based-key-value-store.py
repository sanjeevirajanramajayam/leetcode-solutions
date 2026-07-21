class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # return ""
        bs = self.hashmap[key]
        low = 0
        high = len(bs) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if bs[mid][1] > timestamp: 
                high = mid - 1
            else:
                ans = mid
                low = mid + 1
        if ans == -1:
            return ""
        return bs[ans][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)