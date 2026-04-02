class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> stack;

        for (const string& ops: operations) {
            if (ops == "+") {
                int temp = stack.back(); stack.pop_back();
                int temp2 = stack.back();
                temp2 += temp;
                stack.push_back(temp);
                stack.push_back(temp2);
            } else if (ops == "D") {
                int temp = stack.back();
                temp *= 2;
                stack.push_back(temp);
            } else if (ops == "C") {
                stack.pop_back();
            } else {
                stack.push_back(stoi(ops));
            }
        }
        int sum = 0;
        for (int i = 0; i < stack.size(); i++) {
            sum += stack[i];
        }

        return sum;
    }
};