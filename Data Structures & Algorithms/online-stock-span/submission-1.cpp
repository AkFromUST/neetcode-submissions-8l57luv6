class StockSpanner {
public:
    vector<int> s; vector<int> dp;
    StockSpanner() {
        s = {}; dp = {};
    }
    
    int next(int price) {
        // cout << "Current Price is At: " << price;
        if (s.empty()) {
            s.push_back(price); dp.push_back(1);
            return 1;
        }
        int count = 0;
        while ((s.empty() == false) && s.back() <= price) {
            s.pop_back();
            int span = dp.back(); count += span; dp.pop_back();
            cout << s.size() << " " << dp.size() << endl;
        }
        s.push_back(price);
        count++;
        dp.push_back(count);
        return count;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */