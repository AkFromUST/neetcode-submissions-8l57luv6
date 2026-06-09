class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            temp = [0] * 26
            for c in word:
                temp[ord(c)-ord("a")] += 1
            temp = tuple(temp)
            if temp not in res:
                res[temp] = [word]
            else:
                res[temp].append(word)
        
        
        ans = []
        for k,v in res.items():
            ans.append(v)
        return ans