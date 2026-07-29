class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start = {}
        end = {}
        for i in range(len(s)):
            if s[i] not in start:
                start[s[i]] = i
                end[s[i]] = i
            end[s[i]] = i
        # print(start, end)
        intervals = []
        for key in start:
            intervals.append([start[key], end[key]])
        # print(intervals)
        intervals.sort(key=lambda x : (x[0], x[1]))
        # print(intervals)

        ans = []
        for i in range(len(intervals)):
            if not ans:
                ans.append(intervals[i])
            else:
                if intervals[i][0] <= ans[-1][1]:
                    ans[-1][1] = max(ans[-1][1], intervals[i][1])
                else:
                    ans.append(intervals[i])
        newAns = []
        for start, end in ans:
            newAns.append(end - start + 1)
        print(newAns)
        return newAns
