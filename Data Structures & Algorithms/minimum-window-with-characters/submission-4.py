class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        #ahhh, the concept of taking a sliding window. Then squeezing it until its not valid. That is the min
        l = 0
        n = len(s)

        freq = {}
        values = 0
        for char in t:
            freq[char] = freq.get(char, 0) + 1
        values = len(freq)

        correct_values = 0
        state = {}

        minres = 1001
        minres_pair = ()
        
        for r in range(n):

            char = s[r]
            state[char] = state.get(char, 0) + 1            
            
            if char in freq and state[char] == freq[char]:
                correct_values += 1

            while correct_values == values:
                if (r-l+1) < minres:
                    minres = r-l+1
                    minres_pair = (r, l)
                
                state[s[l]] -= 1
                if s[l] in freq:
                    if state[s[l]] < freq[s[l]]:
                        correct_values -= 1
                l += 1
            
        if minres_pair == ():
            return ""
        return s[minres_pair[1]:minres_pair[0]+1]