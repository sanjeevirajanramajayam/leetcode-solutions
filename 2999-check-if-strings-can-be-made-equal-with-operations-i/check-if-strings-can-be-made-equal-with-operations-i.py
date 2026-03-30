class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        all_combinations = set()

        def swap(s, i, j):
            s = list(s)
            s[i], s[j] = s[j], s[i]
            return "".join(s)
        
        if s1 == s2:
            return True
        
        s_1 = swap(s1, 0, 2)
        s_2 = swap(s1, 1, 3)
        s_3 = swap(s_1, 1, 3)

        all_combinations.add(s_1)
        all_combinations.add(s_2)
        all_combinations.add(s_3)

        if s2 in all_combinations:
            return True
        else:
            return False