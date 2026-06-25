class Solution:
    def _isPandS(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        ans = (s1 == s2[:n1]) and (s1 == s2[n2-n1:])
        return ans
    
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if self._isPandS(words[i], words[j]):
                    count+= 1
        return count