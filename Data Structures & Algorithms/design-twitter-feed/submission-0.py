class Twitter:

    def __init__(self):
        # Global counter to track recency across the entire system
        self.clock = 0
        
        # Maps userId -> list of tweets. 
        # Each tweet is stored as a tuple: (clock_time, tweetId)
        self.tweets = {}
        
        # Maps userId -> set of followeeIds
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.clock += 1
        
        if userId not in self.tweets:
            self.tweets[userId] = []
            
        # CRITICAL TRICK: Insert at index 0 so the list is ALWAYS sorted newest to oldest.
        # This makes reading the timeline later incredibly intuitive!
        self.tweets[userId].insert(0, (self.clock, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        feed = []
        heap = []
        
        # 1. Compile the list of people whose shelves we need to check
        # (The user themselves + anyone they follow)
        target_users = {userId}
        if userId in self.following:
            target_users.update(self.following[userId])
            
        # 2. Grab the absolute newest tweet (index 0) from each user's timeline
        for u_id in target_users:
            if u_id in self.tweets and self.tweets[u_id]:
                time, t_id = self.tweets[u_id][0]
                
                # Max-Heap pattern: -time
                # We store: (-time, tweetId, userId, next_index_to_read)
                heap.append((-time, t_id, u_id, 1))
                
        heapq.heapify(heap)  # <-- Line 1: heapify
        
        # 3. Pull the 10 most recent tweets overall
        while heap and len(feed) < 10:
            neg_time, t_id, u_id, next_idx = heapq.heappop(heap)  # <-- Line 2: heappop
            feed.append(t_id)
            
            # If that specific user has an older tweet on their shelf, push it to the heap
            if next_idx < len(self.tweets[u_id]):
                older_time, older_t_id = self.tweets[u_id][next_idx]
                heapq.heappush(heap, (-older_time, older_t_id, u_id, next_idx + 1))  # <-- Line 3: heappush
                
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # A user shouldn't follow themselves
        if followerId == followeeId:
            return
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)