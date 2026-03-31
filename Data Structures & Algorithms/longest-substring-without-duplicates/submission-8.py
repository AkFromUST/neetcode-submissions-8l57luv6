class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alHash= {}
        l, r = 0 , 1
        
        if len(s) <= 1:
            return len(s)

        alHash[s[0]] = 0
        maxL = 1
        while (r < len(s)) and l < r:
            if s[r] not in alHash or alHash[s[r]] < l:
                print("never seen u before: ", s[r], "/tThe count is: ", r-l + 1, "\tl is: ", l, "\tr is: ", r)
                alHash[s[r]] = r
                maxL = max(maxL, r - l + 1)
            else:
                l = max(alHash[s[r]] + 1, l+1)
                alHash[s[r]] = r
            r += 1
        #print(alHash)
        return maxL