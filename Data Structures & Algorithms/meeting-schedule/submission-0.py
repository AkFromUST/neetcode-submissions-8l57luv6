"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        import heapq

        #Sort the meetings based on the start time
        #can do heapsort if wanted

        heap = []
        start = set()

        for interval in intervals:
            if interval.start in start:
                return False
            else:
                start.add(interval.start)
                heapq.heappush(heap, (interval.start, interval.end))

        res = []

        for i in range(len(intervals)):
            res.append(heapq.heappop(heap))

        for i in range(1, len(intervals)):
            if res[i][0] < res[i-1][1]:
                return False

        return True