class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diffArr = [0] * len(reward1)

        for i in range(len(reward1)):
            diffArr[i] = (reward1[i] - reward2[i], i)
        
        diffArr.sort(key=lambda x: x[0], reverse=True)
        # print(diffArr)
        taken = set()
        ans = 0
        for i in range(k):
            _, ind = diffArr[i]
            taken.add(ind)
            ans += reward1[ind]
        
        for i in range(len(reward2)):
            if i not in taken:
                ans += reward2[i]
        
        return ans