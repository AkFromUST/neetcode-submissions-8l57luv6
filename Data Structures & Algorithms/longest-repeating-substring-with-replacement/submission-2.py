class Solution:
    def _getMaxE(self, state: dict):
        #check if k is less or not. O(26)
        maxV, maxE, total = -1, -1, 0
        for ch,v in state.items():
            if v > maxV:
                maxE = ch
                maxV = v
            total += v
        total -= maxV

        return maxE, maxV, total

    def characterReplacement(self, s: str, k: int) -> int:
        import string
        #sliding window. Condition to shift l: when k < 0.

        l = 0
        longest = 0

        state = {}
        for a in s:
            if a not in state:
                state[a] = 0

        for i in range(len(s)):
            #update state
            state[s[i]] += 1

            maxE, maxV, tempK = self._getMaxE(state)
            
            #check the current val of K.
            while tempK > k:
                #now update the left until k > 0 again 
                state[s[l]] -= 1
                l += 1

                maxE, maxV, tempK = self._getMaxE(state)

            longest = max(longest, i-l+1)

        return longest