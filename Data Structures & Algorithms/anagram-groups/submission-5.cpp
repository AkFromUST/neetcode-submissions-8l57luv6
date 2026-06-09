class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashmap;

        for (const auto& s: strs) {
            //making the vector
            vector<int> freq(26, 0);
            for (char c: s) {
                freq[c - 'a'] += 1;
            }

            // Making it a string
            string key = to_string(freq[0]);
            for (int i = 1; i < 26; ++i) {
                key += "#" + to_string(freq[i]);
            }

            //Now the magic
            hashmap[key].push_back(s);
        }

        //ans
        vector<vector<string>> ans;
        for (const auto& pair: hashmap) {
            ans.push_back(pair.second);
        } 

        return ans;
    }
};
