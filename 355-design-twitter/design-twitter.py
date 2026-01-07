class Twitter(object):

    def __init__(self):
        self.count = 0
        self.followMap = {}
        self.tweetMap = {}

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        minHeap = []
        if userId not in self.followMap:
            self.followMap[userId] = set()
        self.followMap[userId].add(userId)
        for id in self.followMap[userId]:
            if id in self.tweetMap:
                index = len(self.tweetMap[id]) - 1
                count, tweetId = self.tweetMap[id][index]
                minHeap.append((count, tweetId, id, index - 1))
        res = []
        heapq.heapify(minHeap)
        # print(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followerId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followerId][index]
                heapq.heappush(minHeap, (count, tweetId, followerId, index - 1))
        return res

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        if followeeId not in self.followMap[followerId]:
            return
        self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)