class Solution {
public:
    bool _greater(const vector<int>& trips, const vector<int>& target) {
        for (int i = 0; i < 3; ++i) {
            if (trips[i] > target[i]) {
                return true;
            }
        }
        return false;
    }
    
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        // unordered_set<int> target_set;
        // unordered_map<string, vector<int>> hmp; unordered_map<int, string> lookup;

        // int count = 0;
        // for (vector<int>& trips: triplets) {
        //     string key = ""; string lookFor = ""; bool to_skip = false;
        //     for (int i = 0; i < 3; ++i) {
        //         if (trips[i] != target[i]) {
        //             // mising
        //             key += "N";
        //             //but if something exist, then hurray
        //             lookFor += "Y";
        //         } else {
                    
        //             if (trips[i] > target[i]) {
        //                 to_skip = true; break;
        //             }

        //             key += "Y";
        //             lookFor += "N";
        //         }
        //     }
        //     if (to_skip) {continue;}

        //     hmp[key] = trips;
        //     lookup[count] = lookFor;
            
        //     count++;
        //     cout << key << "\t" << lookFor << endl;
        // }

        // for (int i = 0; i < triplets.size();++i) {
        //     vector<int>& trips = triplets[i];
        //     // get the lookup.
        //     string looking = lookup[i];

        //     // does any other trips have this?
        //     if (hmp.contains(looking)) { return true; }
        // }
        // return false;

        vector<vector<int>> smaller = {};
        for (const vector<int>& trips: triplets ) {
            // any value greater than target and skip
            if (!_greater(trips, target)) {
                smaller.push_back(trips);
            }
        }

        if (smaller.empty()) {return false;}

        int n  = smaller.size();
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < 3; ++j) {
                smaller[i][j] = max(smaller[i][j], smaller[i-1][j]);
            }
        }

        return (smaller[n-1] ==target);
    }
};
