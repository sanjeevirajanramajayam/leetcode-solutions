class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start = {}
        end = {}
        for i in range(len(s)):
            if s[i] not in start:
                start[s[i]] = i
                end[s[i]] = i
            else:
                end[s[i]] = i
        intervals = []
        for i in start:
            intervals.append((start[i], end[i]))
        # print(intervals)
        intervals.sort()
        newAns = []
        for start, end in intervals:
            if not newAns:
                newAns.append([start, end])
            else:
                if start <= newAns[-1][1]:
                    newAns[-1][1] = max(newAns[-1][1], end)
                else:
                    newAns.append([start, end])
        ans = []
        for start, end in newAns:
            ans.append(end - start + 1)
        return ans
