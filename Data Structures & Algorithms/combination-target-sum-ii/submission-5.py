class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # Very Similar to Combinations but now we dont allow for retakes.

        candidates.sort()

        res = []
        minE = min(candidates)

        def dfs(index, subset, target):

            if target == 0:
                res.append(subset.copy())
                return

            if index >= len(candidates) or target < minE:
                return
            
            #choosing this one
            subset.append(candidates[index])
            dfs(index + 1, subset, target - candidates[index])
            
            #Not selecting this one
            subset.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            
            dfs(index + 1, subset, target)

        dfs(0, [], target)

        return res