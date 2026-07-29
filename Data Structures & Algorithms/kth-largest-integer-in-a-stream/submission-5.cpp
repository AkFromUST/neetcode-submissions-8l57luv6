class KthLargest {
private:
    priority_queue<int> maxHeap; int k;
public:

    KthLargest(int k, vector<int>& nums): k(k), maxHeap(nums.begin(), nums.end()) {}
    
    int add(int val) {
        maxHeap.push(val);
        vector<int> temp = {};
        for (int i = 0; i < k-1 ; ++i) {
            temp.push_back(maxHeap.top()); maxHeap.pop();
        }
        int res = maxHeap.top();
        for (int& i: temp) {maxHeap.push(i);}
        return res;
    }
};
