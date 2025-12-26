class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        minClosingTime = float('inf')
        penalty = 0
        ans = {}
        for i in range(len(customers)):
            if customers[i] == "Y":
                penalty += 1
        
        ans[penalty] = 0
        minClosingTime = min(penalty, minClosingTime)

        for i in range(len(customers)):
            if customers[i] == "Y":
                penalty -= 1
            else:
                penalty += 1

            if penalty not in ans:
                ans[penalty] = i + 1
            minClosingTime = min(penalty, minClosingTime)
        # print(ans, minClosingTime)
        return ans[minClosingTime]

