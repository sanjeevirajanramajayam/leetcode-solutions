class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        q = deque([i for i in range(len(deck))])
        deck.sort()
        ans = [-1] * len(deck)
        for i in range(len(deck)):
            ans[q.popleft()] = deck[i]
            if q:
                q.append(q.popleft())
        return ans