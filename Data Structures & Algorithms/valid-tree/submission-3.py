class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        #making the adj list - undirected graph
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for edge in edges:
            for i in range(len(edge)):
                if i == 0:
                    continue
                #add the forward edge
                adjList[edge[0]].append(edge[i])
                #add the backward edge
                adjList[edge[i]].append(edge[0])

        seen = set()
        def BFS(node):
            queue = []
            queue.append(node)

            while queue:
                v = queue.pop(0)
                
                for neighbors in adjList[v]:
                    if neighbors not in seen:
                        queue.append(neighbors)
                    
                seen.add(v)
        
        #if connected, all nodes must be in seen
        BFS(0)

        print(seen)
        
        #check if all nodes are connected or not
        for i in range(n):
            if i not in seen:
                return False

        #simple check. If there are more than n-1 edges, there is a cycle and return False. Else return True
        count = 0
        for i in range(n):
            count = count + len(adjList[i])
        
        if count > (2*(n-1)):
            return False
        else:
            return True
