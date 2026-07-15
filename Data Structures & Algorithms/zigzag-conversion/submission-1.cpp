class Solution {
public:
    string convert(string s, int numRows) {
        vector<vector<char>> grid = {}; int n = s.size();
        for (int i = 0;i<numRows;i++) {
            vector<char> temp(n, '#');
            grid.push_back(temp);
        }

        // now the math
        int row = 0; int i = 0; int col = -1; int step = 0;
        while (i < n) {
            row = 0; col++;
            while (i < n && row < numRows) {
                grid[row][col] = s[i];
                row += 1;
                i++;
            }
            col++;
            // now row must be equal to numRows
            row -= 2;
            while (i < n && row >= 1) {
                col++; grid[row][col] = s[i]; row--; i++;
            }
        }

        string res = "";
        for (int i = 0; i < numRows;i++) {
            for (int j = 0; j < n;j++) {
                cout << grid[i][j] << " ";
                if (grid[i][j] != '#') {
                    res += grid[i][j];
                }
            }
            cout << endl;
        }
        return res;
    }
};