class Solution {
public:
    
    int findJudge(int n, vector<vector<int>>& trust) {
        unordered_map<int, int> trusts;
        unordered_set<int> havetrust;

        for (vector<int> &edge: trust) {
            trusts[edge[1]]++;
            havetrust.insert(edge[0]);
        }

        int potential = 0;
        for (auto& kv: trusts) {
            if (kv.second == n-1) {
                potential = kv.first;
            }
        }
        
        if (potential == 0) { return -1; }

        if (havetrust.contains(potential)) {return -1;}
        
        return potential;
    }
};