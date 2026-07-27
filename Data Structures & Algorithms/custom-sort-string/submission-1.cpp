class Solution {
public:
    string customSortString(string order, string s) {
        // priority_queue<pair<int, char>> heap;
        // for (int i = 0; i < order.size(); ++i) {
        //     heap.push(pair<int, char> {-1 * i, order[i]});
        // }
        
        unordered_map<char, int> counter = {};
        unordered_set<char> inS = {};
        unordered_set<char> o (order.begin(), order.end());

        for (auto& c: s) { counter[c]++; inS.insert(c); }

        string res = "";
        for (char& c: order) {
            if (counter[c] != 0) {
                for (int i = 0; i < counter[c]; ++i) {
                    res += c;
                }
            }
        }
        unordered_set<char> seen;
        for (char& c: s) {
            if (o.contains(c) == false && seen.contains(c) == false) {
                seen.insert(c);
                for (int i = 0; i < counter[c];++i) {
                    res += c;
                }
            }
        }

        return res;
    }
};