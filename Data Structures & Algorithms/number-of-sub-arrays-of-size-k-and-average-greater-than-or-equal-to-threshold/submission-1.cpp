class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        // sort(arr.begin(), arr.end());
        double len = 0; double window_sum = 0; int l = 0; int n = arr.size(); int res = 0; double new_avg = 0;
        for (int r = 0; r < n; ++r) {
            window_sum += arr[r]; len++;
            new_avg = window_sum / len;

            while (len > k) {
                window_sum -= arr[l]; len--; l++;
                
            }
            new_avg = window_sum / len;
            if (new_avg >= threshold && len == k) {res++;}
        }
        return res;
    }
};