class Solution:
    def _isSame(self, h1, h2):

        for k,v in h1.items():
            if k not in h2:
                return False
            if v > h2[k]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        
        #ahhh, the concept of taking a sliding window. Then squeezing it until its not valid. That is the min
        l = 0
        n = len(s)

        from collections import Counter
        freq = Counter(t)
        state = {}

        minres = 1001
        minres_pair = ()
        for r in range(n):

            char = s[r]
            state[char] = state.get(char, 0) + 1

            while self._isSame(freq, state): #pretty sure this check is not O(1) but I just want to ensure that the framework is correct
                if (r-l+1) < minres:
                    minres = r-l+1
                    minres_pair = (r, l)
                state[s[l]] -= 1
                if state[s[l]] == 0:
                    del state[s[l]]
                l += 1
            
        if minres_pair == ():
            return ""
        return s[minres_pair[1]:minres_pair[0]+1]