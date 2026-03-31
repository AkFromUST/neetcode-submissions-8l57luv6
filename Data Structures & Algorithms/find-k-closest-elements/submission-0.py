class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        from collections import deque

        l, res = 0, 0
        n = len(arr)
        output = deque()

        #first run
        for i in range(k):
            res += abs(arr[i] - x)
            output.append(arr[i])
    
        for i in range(k, n):

            #state always has len k.
            new_res = abs(arr[i] - x) + res - abs(arr[l] - x)
            l += 1

            if res > new_res:
                res = new_res
                
                output.popleft()
                output.append(arr[i])           

        return list(output)