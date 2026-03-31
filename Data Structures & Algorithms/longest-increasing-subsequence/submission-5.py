class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        import copy

        #the below sol is wrong. O(n^2) is wrong.        

        # res = []
        # for i in range(len(nums)):
        #     incr_subs = 1
        #     temp = i
        #     for j in range(i, len(nums)):
        #         print("considering: ",nums[temp], " and ", nums[j])
        #         if temp != j and nums[j] > nums[temp]:
        #             incr_subs += 1
        #             temp = j
            
        #     res.append(incr_subs)

        # return max(res)

        
        res = []

        def dfs(i, lastelement, currlen):

            #end case. add it to res
            if i == len(nums):
                nonlocal res
                res.append(currlen)
                return

            #dont take
            dfs(i+1, lastelement, currlen)

            #take but only if it satisfies the condition
            if nums[i] > lastelement:
                dfs(i+1, nums[i], currlen + 1)

        dfs(0,-1 * float("inf"), 0)

        return max(res)

            