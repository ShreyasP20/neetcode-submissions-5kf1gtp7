from collections import defaultdict
from heapq import nlargest
from typing import List


class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.user_following = defaultdict(set)
        self.tweets = defaultdict()
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_tweets[userId].append(tweetId)
        self.tweets[tweetId] = self.time

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.user_following[userId]

        users = set(following)
        users.add(userId)

        tweets = [self.user_tweets[user][::-1][:10] for user in users]
        tweets = sum(tweets, [])

        return nlargest(10, tweets, key=lambda tweet_id: self.tweets[tweet_id])


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        following_set = self.user_following[followerId]


        if followeeId in following_set:
            following_set.remove(followeeId)
