class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ans = []
        def fn(ind, string):
            # print(ind)
            if ind == len(s):
                ans.append(string[:len(string) - 1])
                return 
            temp = ""
            for i in range(ind, len(s)):
                temp += s[i]
                if temp in wordDict:
                    fn(i + 1, string + temp +" ")        
            return
        
        fn(0, "")
        return ans
