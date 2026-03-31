class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # isnt the trick the same as the Combination Sum II

        res = []
        nums.sort()
        
        def dfs(index, subset):

            #end case
            if index >= len(nums):
                res.append(subset.copy())
                return

            
            #take this
            subset.append(nums[index])
            dfs(index + 1, subset)

            #dont take this
            subset.pop()

            while (index < len(nums) - 1) and nums[index] == nums[index + 1]:
                index += 1

            dfs(index + 1, subset)

        dfs(0, [])
        
        return res