class Solution {
public:
    string customSortString(string order, string s) {
        unordered_map<char, int> sorted_order;

        int count = 1;
        for (char& c: order) {
            sorted_order[c] = count; count--;
        }

        sort(s.begin(), s.end(), [&]( char a, char b) {
            return sorted_order[a] > sorted_order[b];
        });

        return s;
    }
};