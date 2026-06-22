class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        vector<int> count = {0,0,0};

        for (int& b: bills) {
            if (b == 5) { count[0]++; }
            if (b == 10) {
                if (count[0] <  1) { return false; }
                count[0]--;
                count[1]++;
            }
            if (b == 20) {
                if (count[0] >= 1 && count[1] >= 1) {
                    count[0]--; count[1]--;
                    count[2]++;
                } else if (count[0] >= 3) {
                    count[0] -= 3;
                    count[2]++;
                } else return false;
            }
        }
        return true;
    }
};