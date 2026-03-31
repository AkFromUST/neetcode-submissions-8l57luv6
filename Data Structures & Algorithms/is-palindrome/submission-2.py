class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #pretty easy. Have two pointers, starting at both ends. Check if chars are same or not
        alpha_num = []
        for char in s:
            if char.isalnum():
                alpha_num.append(char.lower())

        i, j = 0, len(alpha_num)-1

        print(alpha_num)

        while (i <= j):
            if (alpha_num[i] != alpha_num[j]):
                return False
            i += 1
            j -= 1
        
        return True