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
                alHash[s[r]] = r
                maxL = max(maxL, r - l + 1)
            else:
                l = max(alHash[s[r]] + 1, l+1)
                alHash[s[r]] = r
            r += 1
        return maxL