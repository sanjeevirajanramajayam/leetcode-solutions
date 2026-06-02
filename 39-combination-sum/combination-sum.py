class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def fn(i, sum, a):
            if i == 0:
                # print(target, sum)
                while sum != target and (target - sum) % candidates[i] == 0:
                    a.append(candidates[i])
                    sum += candidates[i]
                # print(sum, target)
                if sum == target:
                    ans.append(a[:])
                return
            if sum + candidates[i] <= target:
                take = fn(i, sum + candidates[i], a + [candidates[i]])
            not_take = fn(i - 1, sum , a)
        fn(len(candidates) - 1, 0 ,[])
        return ans