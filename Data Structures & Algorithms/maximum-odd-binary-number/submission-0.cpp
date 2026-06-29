class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int n = s.size(); int count = 0;

        for (char& c: s) {
            if (c == '1') {
                count++;
            }
        }
        vector<int> res(n, 0);
        if (count == 1) {
            res[n-1] = 1;
        }
        else {
            res[n-1] = 1;
            count--;
            int index = 0;
            while (count) {
                res[index] = 1;
                count--;
                index++;
            }
        }

        string temp = "";

        for (int& e: res) {
            temp.push_back(char(e + '0'));
        }

        return temp;
        }
};