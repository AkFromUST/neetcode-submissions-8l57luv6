class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        #making adjMap
        adjMap = {}
        for i in range(n):
            adjMap[i] = []
        for edge in edges:
            for i in range(len(edge)):
                if i == 0:
                    continue
                if (edge[i] == edge[0]):
                    continue
                adjMap[edge[0]].append(edge[i])
                adjMap[edge[i]].append(edge[0])
        
        seen = set()
        def BFS(node):
            queue = []
            queue.append(node)
            while queue:
                v = queue.pop()
                for neighbor in adjMap[v]:
                    if (neighbor not in seen):
                        queue.append(neighbor)
                seen.add(v)
            
        count = 0
        for i in range(n):
            if (i not in seen):
                BFS(i)
                count = count + 1
        
        return count