class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        beforeDayGood = [0 for i in range(len(security) + 1)]
        afterDayGood = [0 for i in range(len(security) + 1)]

        for i in range(1, len(security)):
            if security[i - 1] >= security[i]:
                beforeDayGood[i] = 1 + beforeDayGood[i - 1]
            else:
                beforeDayGood[i] = 0
        
        ans = []

        for i in range(len(security) - 2, -1, -1):
            if security[i + 1] >= security[i]:
                afterDayGood[i] = 1 + afterDayGood[i + 1]
            else:
                afterDayGood[i] = 0
        # print(beforeDayGood, afterDayGood)
        for i in range(len(security)):
            if beforeDayGood[i] >= time and afterDayGood[i] >= time:
                ans.append(i)
        
        return ans
