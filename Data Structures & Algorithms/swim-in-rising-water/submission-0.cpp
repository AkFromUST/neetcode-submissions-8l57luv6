#include <cstdlib>

class Solution {
public:
    
    vector<pair<int, int>> nei = {{0,1}, {1,0}, {0,-1}, {-1,0}};

    // dp? Yea I think its Dp
    int _bfs(vector<vector<int>>& grid) {
        int water = 0; int size = grid.size();
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> q; q.push({grid[0][0] ,0,0});
        
        vector<vector<int>> seen(grid.size(), vector<int> (grid[0].size(), 0)); seen[0][0] = 1;
        
        while (q.empty() == false) {
            auto [level, row, col] = q.top(); q.pop();

            water = max(water, level);

            if ((row == grid.size() - 1) && (col == grid[0].size() - 1)) {
                return water;
            }

            for (pair<int, int>& n: nei) {
                int r = row + n.first; int c = col + n.second;

                if (r >= 0 && r < grid.size() && c >= 0 && c < grid[0].size() && seen[r][c] == 0) {
                    q.push({grid[r][c],r,c});
                }
            }
            seen[row][col] = 1;
        }

        return water;
    }
    
    int swimInWater(vector<vector<int>>& grid) {
        return _bfs(grid);
    }
};
