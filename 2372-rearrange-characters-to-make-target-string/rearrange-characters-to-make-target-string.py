class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        hashmap = defaultdict(str)
        hashmap2 = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        mini = float('inf')
        for i in target:
            hashmap2[i] = hashmap2.get(i, 0) + 1
        for i in hashmap2:
            # print( ,hashmap2.get(i, 0) // hashmap2[i])
            mini =  min(hashmap.get(i, 0) // hashmap2[i] , mini) 
        return mini