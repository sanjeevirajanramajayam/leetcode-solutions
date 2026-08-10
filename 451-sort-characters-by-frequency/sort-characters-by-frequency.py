class Solution:
    def frequencySort(self, s: str) -> str:
        buckets = [[] for i in range(len(s) + 1)]
        freqMap = {}

        for i in s:
            freqMap[i] = freqMap.get(i, 0) + 1
        print(freqMap.items())
        for key, value in freqMap.items():
            buckets[value].append(key)
        
        ans = ""
        for i, val in enumerate(buckets):
            for ch in val:
                ans += i * ch

        return ans[::-1]                                



