class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort()
        ans = [0] * len(deck)
        indArr = deque([i for i in range(len(deck))])

        for i in range(len(deck)):
            # print(indArr)
            ind = indArr.popleft()
            ans[ind] = deck[i]
            if indArr:
                indArr.append(indArr.popleft())
        return ans