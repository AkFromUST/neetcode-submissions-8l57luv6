class Solution:
    def jump(self, nums: List[int]) -> int:

        if (len(nums) == 1):
            return 0
        
        dp = []
        
        #dp, stores the min number of turns from that index to end
        for i in range(len(nums)):
            dp.append(-1)

        target = len(nums) - 1

        dp[target] = 0

        #base case
        if (target-1) < 0:
            dp[target-1] = float("inf")
        else:
            dp[target-1] = 1
        
        for i in range(target-2, -1, -1):
            res = float("inf")
            for j in range(1, nums[i] + 1):
                if (i + j) <= target:
                    res = min(res, dp[i+j])
            dp[i] = res + 1

        return dp[0]        
        