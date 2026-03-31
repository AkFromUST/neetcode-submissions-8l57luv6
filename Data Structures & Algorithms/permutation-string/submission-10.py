class Solution:
    def _compare(self, state, act):
        for k, v in act.items():
            if k not in state:
                return False
            if state[k] != v:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_counter = {}
        for c in s1:
            if c not in s1_counter:
                s1_counter[c] = 1
            else:
                s1_counter[c] += 1
        
        state = {}
        import string
        for c in string.ascii_letters:
            state[c] = 0

        state_len = len(s1)
        n = len(s2)
        l = 0

        for r in range(n):
            
            #init
            if r < state_len:
                state[s2[r]] += 1
                continue
            
            if self._compare(state, s1_counter):
                return True
            
            #now the state only needs to be updated
            #remove l. Add r
            state[s2[l]] -= 1
            state[s2[r]] += 1
            l += 1


        #check one last time
        return self._compare(state, s1_counter)
