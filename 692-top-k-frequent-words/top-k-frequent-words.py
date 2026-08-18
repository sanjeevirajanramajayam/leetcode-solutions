class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        buckets = [[] for i in range(len(words))]

        for char, freq in c.items():
            buckets[freq].append(char)
        ans = []
        for i in range(len(words) - 1, -1, -1):
            buckets[i].sort()
            if buckets[i] != []:
                for x in buckets[i]:
                    if k > 0:
                        ans.append(x)
                        k -= 1
                    else:
                        break
        return ans                    