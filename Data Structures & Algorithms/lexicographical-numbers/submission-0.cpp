class Solution {
public:
    vector<int> lexicalOrder(int n) {
        priority_queue<string, vector<string>, greater<string>> maxheap;
        for (int i = 1; i <= n; ++i) {
            string temp = to_string(i);
            maxheap.push(temp);
        }

        vector<int> res;
        while (maxheap.empty() == false) {
            res.push_back(stoi(maxheap.top()));
            maxheap.pop();
        }

        return res;
    }
};
