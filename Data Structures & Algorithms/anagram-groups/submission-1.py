class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # easy.
        res = defaultdict(list)

        for word in strs:
            temp = [0] * 150
            for c in word:
                temp[ord(c)] += 1
            temp = tuple(temp)
            if temp not in res:
                res[temp].append(word)
            else:
                res[temp].append(word)
        
        
        ans = []
        for k,v in res.items():
            ans.append(v)
        return ans