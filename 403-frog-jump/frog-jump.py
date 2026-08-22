class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # distMap = [ {} for i in range(len(stones))]

        # for i in range(len(stones)):
        #     for j in range(i + 1, len(stones)):
        #         distMap[i][stones[j] - stones[i]] = j
        @cache
        def fn(i, k):
            if i == len(stones) - 1:
                return True
            ans = False

            currentIdx = i

            while currentIdx < len(stones) and stones[currentIdx] < stones[i] + k + 1:
                currentIdx += 1
            # print(stones[i], stones[currentIdx])

            if currentIdx < len(stones) and stones[currentIdx] != stones[i] and stones[currentIdx] == stones[i] + k + 1:
                ans = ans or fn(currentIdx, k + 1)
            
            currentIdx = i
            
            while currentIdx < len(stones) and stones[currentIdx] < stones[i] + k:
                currentIdx += 1
            # print(stones[i], stones[currentIdx])

            if currentIdx < len(stones) and stones[currentIdx] != stones[i] and stones[currentIdx] == stones[i] + k:
                ans = ans or fn(currentIdx, k)

            currentIdx = i
            
            while currentIdx < len(stones) and stones[currentIdx] < stones[i] + k - 1:
                currentIdx += 1
            # print(stones[i], stones[currentIdx])
            if currentIdx < len(stones) and stones[currentIdx] != stones[i] and stones[currentIdx] == stones[i] + k - 1:
                ans = ans or fn(currentIdx, k - 1)

            return ans
        
        return fn(0,0)