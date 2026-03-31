class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #thats just too easy
        n = len(trust)
        m = len(trust[0])

        count = {}

        for i in range(n):
            a,b = trust[i][0], trust[i][1]
            count[b] = count.get(b, 0) + 1

        for k, v in count.items():
            if v == n:
                return k

        return -1