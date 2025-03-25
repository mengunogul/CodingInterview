"""
Question: https://neetcode.io/problems/design-twitter-feed
"""

from typing import List
import heapq


class Twitter:
    def __init__(self):
        self.time = 0
        self.users = {}
        self.posts = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId] = self.posts.get(userId, []) + [[self.time, tweetId]]
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.posts.get(userId, [])[:]
        for followee in self.users.get(userId, []):
            feed += self.posts.get(followee, [])
        heapq.heapify(feed)
        return [tid for _, tid in heapq.nlargest(10, feed)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.users.get(followerId, [followerId]):
            self.users[followerId] = self.users.get(followerId, []) + [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users.get(followerId, []) and followeeId != followerId:
            idx = self.users[followerId].index(followeeId)
            del self.users[followerId][idx]


if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 10)  # User 1 posts a new tweet with id = 10.
    twitter.postTweet(2, 20)  # User 2 posts a new tweet with id = 20.
    print(twitter.getNewsFeed(1))  # Expected output: [10]
    print(twitter.getNewsFeed(2))  # Expected output: [20]
    twitter.follow(1, 2)  # User 1 follows user 2.
    print(twitter.getNewsFeed(1))  # Expected output: [20, 10]
    print(twitter.getNewsFeed(2))  # Expected output: [20]
    twitter.unfollow(1, 2)  # User 1 unfollows user 2.
    print(twitter.getNewsFeed(1))  # Expected output: [10]
