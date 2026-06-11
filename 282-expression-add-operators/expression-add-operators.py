class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        
        def fn(curr_idx, currSum, currStr, prev):
            if curr_idx == len(num):
                if currSum == target:
                    ans.append(currStr)
                return 
            temp = ""
            for i in range(curr_idx, len(num)):
                if i > curr_idx and num[curr_idx] == '0':
                    break 
                temp += num[i]
                if curr_idx == 0:
                    fn(i + 1, currSum + int(temp), temp, int(temp))
                else:
                    fn(i + 1, currSum + int(temp), currStr + "+" + temp, int(temp))
                    fn(i + 1, currSum - int(temp), currStr + "-" + temp, -int(temp))
                    fn(i + 1, currSum - prev + int(temp) * prev, currStr + "*" + temp, int(temp) * prev)


        fn(0, 0, "", 0)
        return ans
