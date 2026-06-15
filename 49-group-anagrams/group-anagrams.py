class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        ans = []
        for st in strs:
            hashmap["".join(sorted(list(st)))].append(st)
        for x in hashmap:
            ans.append(hashmap[x])
        return ans