class Solution:
    def countVowelPermutation(self, n: int) -> int:
        charHash = {
            'a' : ('e'),
            'e': ('a', 'i'),
            'i': ('a', 'e', 'o', 'u'),
            'o': ('i', 'u'),
            'u': ('a')
        }
        @cache
        def fn(i, char):
            if i == n:
                return 1
            ans = 0
            for ch in charHash[char]:
                ans += fn(i + 1, ch)
            return ans

        ans = 0
        for i in "aeiou":
            ans += fn(1, i)
        return ans % (10 ** 9 + 7)