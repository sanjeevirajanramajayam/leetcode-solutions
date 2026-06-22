class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = defaultdict(str)
        for i in text:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        return min(hashmap.get('b', 0), hashmap.get('a', 0), hashmap.get('l', 0) // 2, hashmap.get('o', 0) // 2, hashmap.get('n', 0))