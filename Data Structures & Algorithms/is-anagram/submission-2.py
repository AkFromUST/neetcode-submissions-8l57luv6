class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #make a hashmap with freq of occurance for both str. If not same return False, else return True

        h1, h2 = {}, {}

        for char in s:
            if char in h1:
                h1[char] += 1
            else:
                h1[char] = 1
        
        for char in t:
            if char in h2:
                h2[char] += 1
            else:
                h2[char] = 1
        
        h1_key = h1.keys()

        if len(h1) != len(h2):
            return False

        for k,v in h2.items():
            if k not in h1_key:
                return False
        
        for k,v in h1.items():
            if h1[k] != h2[k]:
                return False
        return True