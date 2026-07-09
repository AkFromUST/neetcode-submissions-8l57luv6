class Twitter {
public:
    
    unordered_map<int, unordered_set<int>> followedBy;
    unordered_map<int, unordered_set<int>> following;
    // time, userId, tweetId
    priority_queue<tuple<int, int, int>> tweets;
    int time;

    Twitter(): followedBy({}), following({}), time(0) {}
    
    void postTweet(int userId, int tweetId) {
        // insert this tweet
        time++;
        tweets.push(tuple<int, int, int> {time, userId, tweetId});
        following[userId].insert(userId);
        return ;
    }

    // We keep removing tweets from 
    vector<int> getNewsFeed(int userId) {
        vector<tuple<int, int, int>> tempDB = {};
        vector<int> newsFeed = {};

        while (tweets.empty() == false && newsFeed.size() < 10) {
            auto [time, userid, tweetid] = tweets.top();
            tempDB.push_back(tweets.top());
            tweets.pop();

            if (following[userId].contains(userid)) {
                newsFeed.push_back(tweetid);
            }
        }

        for (auto& e: tempDB) {
            tweets.push(e);
        }

        return newsFeed;
    }
    
    void follow(int followerId, int followeeId) {
        followedBy[followeeId].insert(followeeId);
        following[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        if (followerId == followeeId) {
            return ;
        }
        
        followedBy[followeeId].erase(followeeId);
        following[followerId].erase(followeeId);
    }
};
