class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        cnt = 0
        map = sorted(list(Counter(word).items()), key=lambda x: -x[1])
        # print(map)
        for i in map:
            ans += ((cnt // 8) + 1) * i[1]
            cnt += 1
        return ans