class Solution {
public:
    int _dp(vector<int>& prices, int i, int previ, vector<vector<int>>& cache) {
        
        // no more can be reaped from here on
        if (i == prices.size()) {
            return 0;
        }

        if (cache[i][previ+1] != -1) {return cache[i][previ+1];}

        int res = _dp(prices, i+1, previ, cache);
        if (previ != -1) {
            // that means I bought and now I sell
            res = max(res, prices[i] + _dp(prices, i+1, -1, cache));
        } else {
            // otherwise I buy now
            res = max(res, -prices[i] + _dp(prices, i+1, i, cache));
        }

        return cache[i][previ+1] = res;
    }
    
    int maxProfit(vector<int>& prices) {
        vector<vector<int>> cache(prices.size(), vector<int>(prices.size() + 1, -1));
        return _dp(prices, 0, -1, cache);
    }
};