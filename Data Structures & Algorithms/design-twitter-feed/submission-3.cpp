class Twitter {
public:
    
    unordered_map<int, unordered_set<int>> followedBy;
    unordered_map<int, unordered_set<int>> following;
    // time, tweetId
    unordered_map<int, vector<tuple<int, int>>> tweets;
    int time;

    Twitter(): time(0) {}
    
    void postTweet(int userId, int tweetId) {
        // insert this tweet
        time++;
        tweets[userId].push_back(tuple<int, int> {time, tweetId});
        following[userId].insert(userId);
        return ;
    }

    // We keep removing tweets from 
    vector<int> getNewsFeed(int userId) {
        vector<int> res = {};
        priority_queue<tuple<int, int>> recentTweets = {};

        for (const int& following_id: following[userId]) {
            // get their tweets
            vector<tuple<int, int>> temp = tweets[following_id];
            for (auto& tlist: temp) {
                recentTweets.push(tlist);
            }
        }

        // now get the latest
        while (recentTweets.empty() == false && res.size() < 10) {
            auto [t, ti] = recentTweets.top(); res.push_back(ti);
            recentTweets.pop();
        }

        return res;

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
