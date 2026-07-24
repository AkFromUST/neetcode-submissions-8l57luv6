class Solution {
public:

    int  _dfs(int r, int c, vector<vector<int>>& triangle, vector<vector<int>>& cache) {
        if (r >= triangle.size() || c >= triangle[r].size()) {
            return 0;
        }

        if (cache[r][c] != INT_MAX) {
            return cache[r][c];
        }

        int skip = _dfs(r+1, c+1, triangle, cache);
        int not_skip = _dfs(r+1, c, triangle, cache);

        return cache[r][c] = triangle[r][c] +  min(skip, not_skip);
    } 
    
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<vector<int>> cache (n, vector<int> (0));
        int INF = INT_MAX;
        for (int r = 0; r < triangle.size(); ++r) {
            cache[r].resize(triangle[r].size(), INT_MAX);
        }
        // memset(cache, -1, sizeof(cache));
        return _dfs(0,0,triangle, cache);
    }
};