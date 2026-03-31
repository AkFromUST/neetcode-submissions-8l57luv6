class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = collections.defaultdict(list)

        for u,v,w in times:
            edges[u].append((w,v))

    
        minHeap = [(0,k)]
        heapq.heapify(minHeap)
        seen = set()
        total = 0
        while minHeap:

            w1,n1 = heapq.heappop(minHeap)

            if n1 in seen:
                continue
        
            seen.add(n1)
            total = w1

            for w2,n2 in edges[n1]:
                if n2 not in seen:
                    heapq.heappush(minHeap, (w2 + w1, n2))

        if len(seen) == n:
            return total
        return -1