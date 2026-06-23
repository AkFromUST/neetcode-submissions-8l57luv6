class Solution {
public:
    int findLucky(vector<int>& arr) {
        unordered_map<int, int> freq;
        for (int& num: arr) { freq[num]++; }

        int largest = -1;
        for (auto& items: freq) {
            if (items.second == items.first) {
                largest = max(largest, items.first);
            }
        } return largest;
    }
};