class MedianFinder {
private:
    int size;
    double curr_median;
    priority_queue<int> maxheap;
    priority_queue<int, vector<int>, greater<int>> minheap;
    int minheap_size;
    int maxheap_size;
    int max_element = 1e5 + 1;

public:
    MedianFinder(): size(0), curr_median(1e5 + 1), minheap_size(0), maxheap_size(0){}
    
    void addNum(int num) {
        bool median_lower = false;
        if (size == 0) {
            curr_median = num;
            size++;
            return ;
        }
        else {
            if (curr_median <= num) { median_lower = true; }
            
            // adjusting for size == 1
            if (median_lower && size == 1) {
                maxheap.push(curr_median); maxheap_size++;
            }
            if (!median_lower && size == 1) {
                minheap.push(curr_median); minheap_size++;
            }
            
            if (size % 2 == 0) {
                size++;
                // now the array becames odd.
                if (median_lower) {
                    // about to add to the min_heap
                    minheap.push(num); minheap_size++;
                    // adjust
                    if (abs(minheap_size - maxheap_size) > 1) {
                        maxheap.push(minheap.top()); minheap.pop();
                        maxheap_size++; minheap_size--;
                    }

                    curr_median = minheap.top();
                    return ;
                } else {
                    maxheap.push(num); maxheap_size++;

                    if (abs(minheap_size - maxheap_size) > 1) {
                        minheap.push(maxheap.top()); maxheap.pop();
                        maxheap_size--; minheap_size++;
                    }

                    curr_median = maxheap.top();
                    return ;
                }
            } 
            else {
                if (median_lower) {
                    minheap.push(num); minheap_size++;
                    // adjust
                    if (abs(minheap_size - maxheap_size) > 1) {
                        maxheap.push(minheap.top()); minheap.pop();
                        maxheap_size++; minheap_size--;
                    }
                } else {
                    maxheap.push(num); maxheap_size++;

                    if (abs(minheap_size - maxheap_size) > 1) {
                        minheap.push(maxheap.top()); maxheap.pop();
                        maxheap_size--; minheap_size++;
                    }
                }
                int left_side = maxheap.top();
                int right_side = minheap.top();
                curr_median = (double) (right_side + left_side)  / 2;
                size++;
                return ;
            }
        }
    }
    
    double findMedian() {
        return curr_median;
    }
};
