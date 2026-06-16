class Twitter:

    def __init__(self):
        # users can follow and unfollow: implies hashset
        # userID : set(userID)
        self.timer = 0
        self.users = defaultdict(set)
        # tweets are posted by users with a designated tweetID
        # tweetID is not incremental, so we should have some
        # internal counter to know what is most recent
        # userID: list of tweetID
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        potentialPosts = []
        for whoTweeted, posts in self.tweets.items():
            if whoTweeted in self.users[userId] or whoTweeted == userId:
                # go through posts, append into newsFeed
                for timer, tweetId in posts:
                    heapq.heappush_max(potentialPosts, (timer, tweetId))
        count = 0
        newsFeed = []
        while count < 10 and potentialPosts:
            count += 1
            timer, tweetId = heapq.heappop_max(potentialPosts)
            newsFeed.append(tweetId)
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
