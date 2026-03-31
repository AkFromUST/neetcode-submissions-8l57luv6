class Solution {
public:
    bool isAnagram(string s, string t) {
        // Simply create two hashset
        unordered_map< char, int> s_freq;
        unordered_map< char , int> t_freq;

        //make for s
        int sn = s.size();
        int tn = t.size();

        for (int i = 0; i < sn; i++) {
            char curr = s[i];

            if (!s_freq.count(curr)) {
                s_freq[curr] = 1;
            } else {
                s_freq[curr]++;
            }
        }

        for (int i = 0; i < tn; i++) {
            char curr = t[i];
            if (!t_freq.count(curr)) {
                t_freq[curr] = 1;
            } else {
                t_freq[curr]++;
            }
        }

        int k1 = s_freq.size();
        int k2 = t_freq.size();

        if (k1 != k2) { return false; }
        
        //now check if they are the same or not
        for (const auto& pair: s_freq) {
            char key = pair.first;
            if (!t_freq.count(key)) { return false; }
            else {
                if (s_freq[key] != t_freq[key]) { return false; }
            }
        }
        return true;
    }
};
