class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        long long prev_finish = 0; long long avg_time = 0;

        for (vector<int>& c: customers) {
            int arrive = c[0]; int duration = c[1]; long long extra_waiting_time = 0;

            if (prev_finish == 0 || prev_finish < arrive) {
                extra_waiting_time = 0;
                prev_finish = arrive + duration;
            } else {
                extra_waiting_time = prev_finish - arrive;
                prev_finish += duration;
            }

            avg_time += duration + extra_waiting_time;
        }

        int n = customers.size();
        return (double) avg_time/n;
    }
};