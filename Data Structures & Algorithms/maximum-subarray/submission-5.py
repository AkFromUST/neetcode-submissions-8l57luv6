class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        global_sum = nums[0]
        currS = -1 * float("inf")

        for i in range(len(nums)):

            if currS < 0:
                currS = 0

            currS += nums[i]
            global_sum = max(global_sum, currS)


        return global_sum