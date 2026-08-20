class Solution {
public:
    
    int _bs_row(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size(); int col = matrix[0].size(); int l = 0; int r = rows - 1; long long mid = 0;
        while (l <= r) {
            mid = (r+l) / 2;
            if (target >= matrix[mid][0] && target <= matrix[mid][col-1]) {
                return mid;
            }
            else {
                if (target < matrix[mid][0]) {
                    r = mid - 1;
                } else if (target > matrix[mid][col-1]) {
                    l = mid + 1;
                }
            }
        }
        return -1;
    }
    
    bool _bs(vector<vector<int>>& matrix, int target, int row) {
        // do a bs
        int col = matrix[0].size(); int l = 0; int r = col - 1; long long mid= 0;
        while (l <= r) {
            mid = (r+l)/2;
            if (matrix[row][mid] == target) {
                return true;
            }
            if (matrix[row][mid] > target) {
                r = mid - 1;
            } else if (matrix[row][mid] < target) {
                l = mid + 1;
            }
        }
        return false;
    }
    
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty()) {
            return false;
        }
        int row = matrix.size(); int col = matrix[0].size();

        if (row == 1 && col == 1) {
            return (matrix[0][0] == target);
        }

        int r = _bs_row(matrix, target);
        if (r == -1) return false;
        return _bs(matrix, target, r);
    }
};
