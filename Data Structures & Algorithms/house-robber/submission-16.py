class Solution:
    def rob(self, nums: List[int]) -> int:
        
        """
        #below backtracking solution is logically correct. Work on making the DP relation from here:

        #lets make the backtracking first
        res = -1 * float("inf")
        
        def backtracking(index, totalCost, lastIndex):
            #end case
            if index >= len(nums):
                nonlocal res
                res = max(res, totalCost)
                return

            #rob this house only if lastIndex != index - 1
            if (index > 0 and lastIndex != (index - 1)) or lastIndex == -1:
                backtracking(index + 1, totalCost + nums[index], index)

            #dont rob this house
            backtracking(index + 1, totalCost, lastIndex)
        
        backtracking(0, 0, -1)

        return res
        """

        #Below is the bottom-up approach. The decision tree does not really help in this

        n = len(nums)

        if n == 0:
            return 0

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        nums.append(0)

        #init memoisation
        dp = [0] * (n+1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n+1):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[n]
















                