class Solution:
    def rotatedDigits(self, n: int) -> int:
        bad_nums = set([3, 4, 7])
        good_nums = set([2, 5, 6, 9])

        def check(x):
            good_check = False
            for i in str(x):
                if int(i) in bad_nums:
                    return False
                if int(i) in good_nums:
                    good_check = True
            return good_check
        cnt = 0
        for i in range(n + 1):
            if check(i):
                cnt += 1
        return cnt