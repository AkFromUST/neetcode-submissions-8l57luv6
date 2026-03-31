class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # Very Similar to Combinations but now we dont allow for retakes.

        res = []
        minE = min(candidates)

        def dfs(index, subset, target):

            if target == 0:
                
                #check if this already exists in res or not

                temp = set()
                for n in subset:
                    temp.add(n)


                add = True
                for ls in res:
                    present = True
                    for currN in ls:
                        if currN not in temp:
                            present = False

                    if present:
                        add = False
                        break
                
                if add:
                    res.append(subset.copy())
                return

            if index >= len(candidates) or target < minE:
                return

            #choosing this one
            subset.append(candidates[index])
            dfs(index + 1, subset, target - candidates[index])
            
            #Not selecting this one
            subset.pop()
            dfs(index + 1, subset, target)

        dfs(0, [], target)

        return res

        # temp = []

        # for ls in res:
        #     temp.append(tuple(ls))

        # res = set()

        # for ls in temp:
        #     res.add(ls)

        # print(res)

        # temp = []
        # for tpl in res:
        #     temp.append(list(tpl))

        # return temp