class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if (len(s) != len(t)):
            return False

        hash1 = {}
        hash2 = {}

        for i in range(len(s)):
            if s[i] in hash1.keys():
                hash1[s[i]] = hash1[s[i]] + 1
            else:
                hash1[s[i]] = 1
            
            if t[i] in hash2.keys():
                hash2[t[i]] = hash2[t[i]] + 1
            else:
                hash2[t[i]] = 1

        for keys in hash1.keys():
            if keys not in hash2.keys():
                return False
            
            if hash1[keys] != hash2[keys]:
                return False

        return True