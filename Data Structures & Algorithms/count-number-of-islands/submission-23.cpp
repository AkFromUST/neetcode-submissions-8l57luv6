class Solution {
public:
    void _dfs(int r, int c, vector<vector<char>> &grid, int row, int col) {
        
        stack<pair<int, int>> s; s.push({r,c}); vector<pair<int, int>> nei = {{0,1}, {1,0}, {0,-1}, {-1,0}};
        
        while (s.empty() == false) {
            int dx = s.top().first; int dy = s.top().second; s.pop();

            for (auto& n: nei) {
                int nx = dx + n.first; int ny = dy + n.second;

                if ((nx >= 0 && nx < row) && (ny >= 0 && ny < col) && grid[nx][ny] == '1') {
                    // now we can make this 0
                    grid[nx][ny] = '0'; s.push({nx,ny});
                }
            }
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int row = grid.size(); int col = grid[0].size(); int count = 0;

        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                if (grid[i][j] ==  '1') {
                    _dfs(i,j, grid, row, col);
                    count++;
                }
            }
        } return count;
    }
};
