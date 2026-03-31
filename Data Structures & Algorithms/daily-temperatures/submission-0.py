class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
            Brute Force <> O(n^2)
            Stack (potentially, minstack) <> O(n)
        """

        from collections import deque

        minq = deque()
        n = len(temperatures)
        res = [0] * n
        
        for i in range(n):

            if not minq:
                minq.append((temperatures[i], i))
                continue

            curr = temperatures[i]

            #otherwise curr is greater than the most min we know
            while minq and curr > minq[0][0]:
                prev, previ = minq.popleft()
                #appends to the result
                result = i - previ
                res[previ] = result

            minq.appendleft((curr, i))
            

        return res