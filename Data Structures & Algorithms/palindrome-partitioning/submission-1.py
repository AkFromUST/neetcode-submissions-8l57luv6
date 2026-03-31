class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        #backtracking. There are two options, include this char or not include this char.
        #But it must be a substring. Substring are contigious

        if not s:
            return []

        def _isPal(x): #O(n)
            if not x:
                return False

            i, j = 0, len(x) - 1
            while i <= j:
                if x[i] != x[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        res = []
        
        def backtracking(start, end, curr):
            
            if end >= len(s):
                if start == end:
                    res.append(curr.copy())
                return

            #check if its so far palindrome or not
            # print("checking if str is a pal or not: ", s[start:end+1])
            # print("\t\tstart: ", start, "\tend: ", end)
            if _isPal(s[start:end+1]):
                #print("\t\tmade it")
                curr.append(s[start:end+1])
                
                #partition here
                backtracking(end + 1, end + 1, curr)
                curr.pop()

            #dont partition it
            backtracking(start, end + 1, curr)

    
        backtracking(0, 0, [])

        return res