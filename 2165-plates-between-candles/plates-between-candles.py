class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        aCount = [0] * n
        left = [0] * n
        right = [0] * n

        if s[0] == '*':
            aCount[0] += 1

        if s[0] == '|':
            left[0] += 1

        if s[n - 1] == '|':
            right[n - 1] = n - 1

        for i in range(1, len(s)):
            if s[i] == '*':
                aCount[i] = aCount[i - 1] + 1
            else:
                aCount[i] = aCount[i - 1]

            if s[i] == '|':
                left[i] = i
            else:
                left[i] = left[i - 1]

        for i in range(len(s) - 2, -1, -1):
            if s[i] == '|':
                right[i] = i
            else:
                right[i] = right[i + 1]

        # temp = right
        # right = left
        # left = temp
        ans = []
        for start, end in queries:
            lefte = right[start]
            righte = left[end]
            # print(start, end, lefte, righte)
            if not (lefte >= start and lefte <= end)  or not (righte >= start and righte <= end):
                ans.append(0)
                continue
            ans.append(aCount[righte] - aCount[lefte])
        return ans