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
                if (edge[0] == edge[i]):
                    return False
                #add the forward edge
                adjList[edge[0]].append(edge[i])
                #add the backward edge
                adjList[edge[i]].append(edge[0])

        seen = set()
        parent = [-1 for i in range(n)]
        def BFS(node):
            queue = []
            queue.append(node)
            while queue:
                v = queue.pop(0)
                for neighbors in adjList[v]:
                    if neighbors not in seen:
                        parent[neighbors] = v
                        queue.append(neighbors)
                    else:
                        # i have seen this node before.
                        # That means if its not a cycle
                        # v must be the parent of this node
                        if (parent[v] != neighbors):
                            return False
                seen.add(v)
            return True
        
        #if connected, all nodes must be in seen
        if (BFS(0) == False):
            return False
        else:
            for i in range(n):
                if i not in seen:
                    return False
            return True
        
        # #check if all nodes are connected or not
        # for i in range(n):
        #     if i not in seen:
        #         return False

        # #simple check. If there are more than n-1 edges, there is a cycle and return False. Else return True
        # #since its an undirected graph. There must not be more than 2 * (n-1) edges.
        # count = 0
        # for i in range(n):
        #     count = count + len(adjList[i])
        
        # if count > (2*(n-1)):
        #     return False
        # else:
        #     return True
