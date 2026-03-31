class Solution:
    def canPartition(self, nums: List[int]) -> bool:     
        """
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
        """
        
        #lets try to optimize it

        n = len(nums)
        remS = 0
        for j in range(n):
            remS += nums[j]

        if remS % 2 != 0:
            return False
        
        memo = {}

        def dfs(i,s1,s2):
            
            #end case
            if i == len(nums):
                if s1 == s2:
                    memo[(i, s1)] = True
                    return True
                memo[(i, s2)] = False
                return False
            
            #Two decisions. Not take and Take
            if (i, s1) in memo:
                return memo[(i, s1)]

            #not take
            t1 = dfs(i+1, s1, s2)

            #take
            t2 = dfs(i+1, s1 + nums[i], s2 - nums[i])

            memo[(i,s1)] = t1 or t2

            return t1 or t2

        res = dfs(0,0,remS)

        return res