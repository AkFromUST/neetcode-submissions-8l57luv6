class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        import copy        
        #backtracking. Can keep track of only one subset and can infer the rest

        def dfs(i, s1, s2):

            #end case. Check the end conditions here
            if i == len(nums):
                if s1 == s2:
                    return True
                return False
            
            #not take
            t1 = dfs(i+1, s1, s2 + nums[i])

            #take
            t2 = dfs(i+1, s1  + nums[i], s2)
            
            return t1 or t2

        return dfs(0, 0, 0)

        #lets try to optimize it