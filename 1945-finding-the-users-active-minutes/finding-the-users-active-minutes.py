class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        hash = {}
        for user_id, action in logs:
            if user_id not in hash:
                hash[user_id] = set()
            hash[user_id].add(action)
        
        ans = [0 for i in range(k)]

        for id in hash:
            ans[len(hash[id]) - 1] += 1
        
        return ans
