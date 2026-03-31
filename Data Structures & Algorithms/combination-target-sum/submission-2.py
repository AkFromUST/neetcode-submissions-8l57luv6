class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        #This cant use the same sol as the before question since each element can be used more than once
        
        res = []
        minE = min(nums)
        def backtracking(target, index, subset):

            if target == 0:
                res.append(subset.copy())
                return

            if target < minE:
                return

            if index >= len(nums) or target < 0:
                return

            subset.append(nums[index])

            #consider index element
            backtracking(target - nums[index], index, subset)
            #backtracking(target-nums[index], index + 1, subset)
            
            #dont consider this index element
            subset.pop()
            backtracking(target, index + 1, subset)

        backtracking(target, 0, [])


        #some nuances in the return type. Not sure if this is the most optimal or not

        temp = []
        for ls in res:
            temp.append(tuple(ls))
        
        combs = set()

        for tpl in temp:
            combs.add(tpl)

        res = []

        for ls in combs:
            res.append(list(ls))

        return res