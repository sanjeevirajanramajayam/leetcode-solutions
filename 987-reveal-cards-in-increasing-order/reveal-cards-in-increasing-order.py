class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort()
        queue = deque([i for i in range(len(deck))])
        ans = [1 for i in range(len(deck))]

        for j in range(len(deck)):
            i = queue.popleft()
            ans[i] = deck[j]
            if queue:
                queue.append(queue.popleft())
        return ans

