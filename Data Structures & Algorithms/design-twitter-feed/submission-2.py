class Twitter:

    def __init__(self):
        self.followings = defaultdict(set)
        self.global_feed = list()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.global_feed.insert(0, tuple([userId, tweetId]))

    def getNewsFeed(self, userId: int) -> List[int]:
        result = list()
        for tweeterId, tweetId in self.global_feed:
            if len(result) == 10:
                break
            if userId == tweeterId or tweeterId in self.followings[userId]:
                result.append(tweetId)
        return result
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].discard(followeeId)