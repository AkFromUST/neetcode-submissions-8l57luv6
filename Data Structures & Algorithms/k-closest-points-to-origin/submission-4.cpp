class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<float, vector<int>>> heap;

        for (auto coor: points) {
            int x1 = coor[0] * coor[0]; int y1  = coor[1] * coor[1];
            int dist = x1 + y1;
            pair<int, vector<int>> temp = {dist * -1, coor};
            heap.push(temp);
        }

        vector<vector<int>> res = {};
        while (k > 0) {
            res.push_back(heap.top().second); heap.pop(); k--;
        }
        return res;
    }
};
