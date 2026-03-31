class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        import copy        
        #backtracking. Can keep track of only one subset and can infer the rest

        def dfs(i, subs1):

            #end case. Check the end conditions here
            if i == len(nums):
                s1, s2 = 0, 0
                
                if not subs1 or len(subs1) == 0:
                    return False

                print("Subs1 <>")
                for i in range(len(nums)):
                    
                    if i in subs1:
                        s1 += nums[i]
                        print("\tSubs1 elements are: ", nums[i])
                    else:
                        s2 += nums[i]
                    
                if s1 == s2:
                    return True
                return False
            
            #not take
            t1 = dfs(i+1, subs1)

            #take
            temp = copy.deepcopy(subs1)
            temp.append(i)
            t2 = dfs(i+1, temp)
            
            return t1 or t2

        return dfs(0, [])