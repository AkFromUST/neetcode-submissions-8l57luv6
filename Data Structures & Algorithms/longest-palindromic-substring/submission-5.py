class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #if we use two pointers, then the sol is O(n^2) right?

        #final vars values are here
        finalL, finalR, longest = -1, -1, -1
        
        #first check for odd length
        for i in range(len(s)):

            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                print("l: ", l, "\tr: ", r, "\t\tvalue at l: ", s[l], "\tvalue at r: ", s[r])
                l -= 1
                r += 1
            l += 1
            r -= 1
            if (r-l+1) > longest:
                print("found a new longest: ", s[l:r+1], "l: ", l, "r: ", r)
                longest = r - l + 1
                finalL, finalR = l, r

        #checking for even length
        for i in range(len(s)):

            l, r = i - 1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                print("l: ", l, "\tr: ", r, "\t\tvalue at l: ", s[l], "\tvalue at r: ", s[r])
                l -= 1
                r += 1

            l += 1
            r -= 1
            if (r-l+1) > longest:
                print("found a new longest: ", s[l:r+1], "l: ", l, "r: ", r)
                longest = r - l + 1
                finalL, finalR = l, r

        return s[finalL:finalR+1]