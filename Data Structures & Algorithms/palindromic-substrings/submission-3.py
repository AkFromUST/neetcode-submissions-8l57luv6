class Solution:
    def countSubstrings(self, s: str) -> int:
        
        """
        #brute force <- get all substrs and check each one of them if they are a palindrome or not

        all_substr= []

        for i in range(len(s)):
            for j in range(i,len(s)):
                all_substr.append(s[i:j+1])

        def _checkPalin(text):
            i,j = 0, len(text) - 1

            while i <= j:
                if text[i] != text[j]:
                    return False
                i += 1
                j -= 1

            return True

        count = 0
        for ss in all_substr:
            if _checkPalin(ss):
                count += 1
        
        return count
        """

        #same logic as the prev one
        total = 0

        #lets check odd length first
        for curr in range(len(s)):
            i,j = curr - 1, curr + 1
            print(i,j)

            while i >= 0 and j < len(s) and s[i] == s[j]:
                total += 1
                i -= 1
                j += 1

        
        #lets check even length now
        for curr in range(len(s)):
            l,r = curr - 1, curr
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1

        return total + len(s)