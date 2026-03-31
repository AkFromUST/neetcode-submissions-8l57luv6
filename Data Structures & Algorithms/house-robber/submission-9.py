class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # same as the prev question except now you are maximising

        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        temp = [0]
        for num in nums:
            temp.append(num)
        nums = temp

        dp = [0] * (n +1)
        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[2])
        
        for i in range(3, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[n]
