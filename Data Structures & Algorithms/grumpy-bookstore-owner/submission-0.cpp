class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        // fixed window
        int maxres = 0; int satisfied = 0; int l = 0; int window = 0;

        for (int r = 0; r < customers.size(); ++r) {
            if (grumpy[r] == 1) {
                window += customers[r];
            } else {
                satisfied += customers[r];
            }

            if (r-l+1 > minutes) {
                if (grumpy[l] == 1) {
                    window -= customers[l];
                } l++;
            }

            maxres = max(maxres, window);
        }

        return maxres + satisfied;
    }
};