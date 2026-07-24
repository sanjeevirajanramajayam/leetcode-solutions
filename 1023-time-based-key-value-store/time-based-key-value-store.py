class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        bs = self.hashmap[key]
        low = 0
        high = len(bs) - 1
        ans = ""
        while low <= high:
            mid = (low + high) // 2
            val = bs[mid][0]
            if val == timestamp:
                return bs[mid][1]
            elif val > timestamp:
                high = mid - 1
            else:
                ans = bs[mid][1]
                low = mid + 1
        return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)