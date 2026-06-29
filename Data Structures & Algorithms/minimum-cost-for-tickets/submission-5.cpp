class Solution {
public:
    unordered_map<int, int> dp;

    // i represents the day that we have to pay for. So we are covered until i-1 days.
    int _backtracking(int cost, int max_day, int i, vector<int> &costs, int dindex, vector<int> &days) {
        while (dindex < days.size() && (i - 1) >= days[dindex]) {
            dindex++;
        }

        if (dindex >= days.size()) {
            return cost;
        }

        if (dp.contains(dindex)) {
            return cost + dp[dindex];
        }

        if (days[dindex] > (i - 1)) {
            i = days[dindex];
        }

        int r1 = _backtracking(cost + costs[0], max_day, i + 1, costs, dindex, days);
        int r2 = _backtracking(cost + costs[1], max_day, i + 7, costs, dindex, days);
        int r3 = _backtracking(cost + costs[2], max_day, i + 30, costs, dindex, days);

        int res = min({r1, r2, r3});

        dp[dindex] = res - cost;
        return res;
    }
    
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int max_day = days.back();
        return _backtracking(0, max_day, days[0], costs, 0, days);
    }
};