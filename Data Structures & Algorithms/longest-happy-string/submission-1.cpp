class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        int limit = 3;
        string res = "";

        priority_queue<tuple<int, char>> maxHeap;
        maxHeap.push(tuple<int, char> {a, 'a'});
        maxHeap.push(tuple<int, char> {b, 'b'});
        maxHeap.push(tuple<int, char> {c, 'c'});

    
        while (maxHeap.empty() == false) {
            // first get the back
            auto [count, c] = maxHeap.top(); maxHeap.pop();

            if (count == 0) {
                return res;
            }
            
            // checking for the length type
            if (res.size() >= 2) {
                int n = res.size();
                if ((res[n-1] == c) && (res[n-2] == c)) {
                    // get the second largest
                    auto [count2, c2] = maxHeap.top(); maxHeap.pop();

                    if (count2 == 0) {
                        return res;
                    }
                    res += c2;
                    
                    maxHeap.push(tuple<int, char> {count2-1, c2});
                    maxHeap.push(tuple<int, char> {count, c});
                    continue;
                }
            }


            
            res += c;
            maxHeap.push(tuple<int, char> {count-1, c});
        }

        return res;

        
    }
};