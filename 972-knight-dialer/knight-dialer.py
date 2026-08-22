class Solution:
    def knightDialer(self, n: int) -> int:
        numsHash = {
            "1" : ("6", "8"),
            "2" : ("7", "9"),
            "3" : ("4", "8"),
            "4" : ("3", "9", "0"),
            "5" : (),
            "6" : ("1", "7", "0"),
            "7" : ("2", "6"),
            "8" : ("1", "3"),
            "9" : ("2", "4"),
            "0" : ("4", "6")
        }
        @cache
        def fn(i, num):

            if i == n - 1:
                # print(i, num, "end")
                return 1
            # print(i, num)
            ans = 0
            for ch in numsHash[num]:
                ans += fn(i + 1, ch)
            return ans
        ans = 0
        for i in range(0, 10):
            ans += fn(0, str(i))
        return ans % (10 ** 9 + 7)