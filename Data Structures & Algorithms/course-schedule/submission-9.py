class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
            Can we think of pre-req as a adj_list. Index represents the node and adj_list[i] represents the node its connected to (including itself)
            Also if thats the case, can we assume that the first element is always the index? (logically derived)

            correction -> this is a wrong assumption
            Test case that contradicts the above:
                numCourses=5
                prerequisites=[[1,4],[2,4],[3,1],[3,2]]
                output: True
        """

        """
            Method 1: If Cycle detected, return False. This is the right ans
        """

        preMap = {}
        for i in range((numCourses)):
            preMap[i] = []

        for lis in prerequisites:
            for i in range(len(lis)):
                if i == 0:
                    continue
                preMap[lis[0]].append(lis[i])
        
        visiting = set()
        def DFS(course):
            if (course in visiting):
                return False
            if (preMap[course] == []):
                return True

            visiting.add(course)
            #process all neighbours
            for v in preMap[course]:
                if not DFS(v):
                    return False
            visiting.remove(course)
            preMap[course] = []
            return True

        for i in range(numCourses):
            if not DFS(i):
                return False
        return True        