class Solution {
public:
    
    int orangesRotting(vector<vector<int>>& grid) {
        int n = grid.size(); int m = grid[0].size();
        vector<vector<int>> nei = {{1,0}, {0,1}, {-1,0}, {0,-1}}; queue<vector<int>> rotten;
        int time = 0; int fresh_fruits = 0;

        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                if (grid[r][c] == 2) rotten.push({r, c, 0});
                if (grid[r][c] == 1) fresh_fruits++;
            }
        }
        if (fresh_fruits == 0) return 0;
        if (rotten.empty()) return -1;

        while (!rotten.empty()) { 
            vector<int> temp = rotten.front(); rotten.pop();
            int row = temp[0]; int col = temp[1]; int layer = temp[2];

            for (vector<int>& ne: nei) {
                int new_r = row + ne[0]; int new_c = col + ne[1];
                if (new_r >=0 && new_r < n && new_c >= 0 && new_c < m && grid[new_r][new_c] == 1) {
                    rotten.push({new_r, new_c, layer + 1});
                    grid[new_r][new_c] = 2;
                }
            }
            time = max(time, layer);
        }

        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                if (grid[r][c] == 1) return -1;
            }
        }

        return time;
    }
};
