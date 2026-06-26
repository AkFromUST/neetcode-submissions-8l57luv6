class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        unordered_map<char, int> last; int largest = -1;

        for (int i = 0; i < s.size(); i++) {
            char c = s[i];
            
            if (last.contains(c)) {
                largest = max(largest, i - last[c]-1);
            } else { last[c] = i; }
        }

        return largest;

    }
};