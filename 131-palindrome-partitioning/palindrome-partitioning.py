class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def fn(ind, arr):
            # print(ind)
            if ind == len(s):
                ans.append(arr)
                return 
            temp = ""
            for i in range(ind, len(s)):
                temp += s[i]
                if temp == temp[::-1]:
                    fn(i + 1, arr + [temp])       
            return
        
        fn(0, [])
        return ans
