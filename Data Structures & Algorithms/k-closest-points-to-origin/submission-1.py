class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dist = (x**2) + (y**2)
            dist = dist ** 0.5
            heapq.heappush(heap, (dist, [x,y]))

        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        return output