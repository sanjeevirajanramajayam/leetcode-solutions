class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote) 
        b = Counter(magazine)
        for x in a:
            if b.get(x, 0) < a[x]:
                return False
        return True