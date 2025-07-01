from collections import defaultdict
import heapq
from typing import List
"""
This is an implementation of a simplified Twitter clone, supporting tweeting, following/unfollowing, and fetching a user's news feed.

--> Key Functionalities:
- Users can post tweets.
- Users can follow or unfollow other users.
- The news feed returns the 10 most recent tweets from the user and people they follow.

--> Data Structures:
- `self.posts`: A defaultdict that maps each user to a list of their tweets, stored as tuples (-timestamp, tweetId).
- `self.followers`: A defaultdict mapping each user to the set of users they follow.
- `self.count`: A global decreasing counter used to simulate timestamps (ensuring newer tweets have smaller values for max-heap behavior).

--> Time Complexity
- postTweet(): O(1)
- follow() / unfollow(): O(1)
- getNewsFeed():
    - Worst case O(n log n), where n is the total number of tweets from the user and their followees.
    - But usually performs faster in practice due to a limited number of tweets being heapified.

--> Space Complexity
- O(u + t), where:
    - u is the number of users.
    - t is the total number of tweets stored.

--> Approach:
- When `getNewsFeed()` is called:
    - Gather all tweets from the user and their followees.
    - Use a min-heap to keep track of the 10 most recent tweets (since we use negative timestamps, the smallest number is the most recent).
    - Return the tweet IDs in order of recency.

This design balances simplicity with efficiency and is suitable for simulating basic Twitter-like operations.
"""
class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.followers = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.count, tweetId))
        self.count -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        recent_tweets = []
        for followers in self.followers[userId]:
            for tweet in self.posts[followers]:
                tweets.append(tweet)
        for tweet in self.posts[userId]:
            tweets.append(tweet)
            
        heapq.heapify(tweets)

        while len(recent_tweets) < 10 and tweets:
            _, tweetId = heapq.heappop(tweets)
            recent_tweets.append(tweetId)

        return recent_tweets
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)