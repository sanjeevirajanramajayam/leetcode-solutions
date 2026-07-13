class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        # for i in string.digits:
        digits = list(string.digits)[1:]
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                # print(i, j)
                ans.append(int("".join(digits[i:j + 1])))
        # print(ans)
        ans.sort()
        # print(ans)
        start_ind = bisect_left(ans, low - 1)
        end_ind = bisect_left(ans, high + 1)
        return (ans[start_ind:end_ind])