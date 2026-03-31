class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        

        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:

            #popping the two heaviest stone
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            if (-1 * s1) > (-1 * s2):
                s1 = ((-1 * s1) - (-1 * s2)) * -1
                heapq.heappush(stones, s1)
            else:
                s2 = ((-1 * s2) - (-1 * s1)) * -1
                heapq.heappush(stones, s2)

        if stones:
            return -1 * stones[0]
        return 0