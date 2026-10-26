class Solution {
public:

    unordered_map<char, int> _djikstra(char source, unordered_map<char, pair<vector<char>, vector<int>>>& adjmap) {
        priority_queue<pair<int, char>, vector<pair<int, char>>, greater<pair<int, char>>> minheap;
        
        minheap.push({0, source});
        unordered_map<char, int> min_cost;

        while (!minheap.empty()) {
            // get the cheapest option
            pair<int, char> adj = minheap.top(); minheap.pop();
            
            if (min_cost.contains(adj.second)) continue;
            min_cost[adj.second] = adj.first;

            pair<vector<char>, vector<int>> n = adjmap[adj.second];
            int s = n.first.size();
            for (int i = 0; i < s; ++i) {
                minheap.push({n.second[i] + adj.first, n.first[i]});
            }
        }

        return min_cost;
    }
    
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        
        // I think this is a djikstra problem
        unordered_map<char, pair<vector<char>, vector<int>>> adjmap = {};
        int n = original.size(); int s = source.size(); unordered_map<char, unordered_map<char, int>> conversion;

        for (int i = 0; i < n; ++i) {
            adjmap[original[i]].first.push_back(changed[i]);
            adjmap[original[i]].second.push_back(cost[i]);
        }
        vector<int> seen(26, 0);
        for (char& c: source) {
            if (seen[c-'a'] == 0) {
                conversion[c] = _djikstra(c, adjmap);
                seen[c-'a']++;
            }
        }

        long long res_cost = 0;
        for (int i = 0; i < s; ++i) {
            if (source[i] == target[i]) continue;

            if (conversion[source[i]].contains(target[i]) == false) return -1;
            res_cost += conversion[source[i]][target[i]]; 
        }

        return res_cost;
        
    }
};
 