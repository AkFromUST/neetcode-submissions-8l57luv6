class Solution:
    def longestPalindrome(self, s: str) -> str:
        #dp, there are only two sub sequences that you have to find

        if (len(s) == 1):
            return s


        temp_max = ""
        for i in range(len(s)):
            temp = s[i]
            l = r = i
            while (r < len(s) and l > -1) and (s[l] == s[r]):
                temp = s[l:r+1]
                if (len(temp) > len(temp_max)):
                    temp_max = temp
                l -= 1
                r += 1
            
            #even case:
            l = i
            r = i+1
            while (r < len(s) and l > -1) and (s[l] == s[r]):
                temp = s[l:r+1]
                if (len(temp) > len(temp_max)):
                    temp_max = temp
                l -= 1
                r += 1

                
        return temp_max