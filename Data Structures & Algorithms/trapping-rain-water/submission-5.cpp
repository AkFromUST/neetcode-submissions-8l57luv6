class Solution {
public:
    int trap(vector<int>& height) {
        //ceiling is min(l, r) 
        int prev_height = 0; int r = 0; int n = height.size(); int close = 0; vector<pair<int, int>> monostack = {}; int total = 0;

        while (r < n) {
            
            while (monostack.empty() == false && monostack.back().second <= height[r]) {                
                int minHeight = monostack.back().second;
                int width = r - monostack.back().first - 1;
                total += (minHeight - prev_height) * width;
                prev_height = monostack.back().second;
                monostack.pop_back();
                // cout << height[r] << "\ttotal: " << total << endl;
            }

            if (monostack.empty()) { prev_height = 0; }
            else {
                if (monostack.back().second > height[r]) {
                    total += (height[r] - prev_height) * (r - monostack.back().first - 1);
                }
                
            }
            monostack.push_back({r, height[r]});
            r++;
        }

        return total;
    }
};
