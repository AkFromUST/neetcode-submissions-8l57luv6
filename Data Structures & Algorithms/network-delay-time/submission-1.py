class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))


        minH = [(0, k)]
        visit = set()
        total = 0
        while minH:
            w1, n1 = heapq.heappop(minH)

            if n1 in visit:
                continue
            
            visit.add(n1)
            total = w1

            for n2, w2, in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minH, (w1 + w2, n2))
            
        if len(visit) == n:
            return total
        return -1
