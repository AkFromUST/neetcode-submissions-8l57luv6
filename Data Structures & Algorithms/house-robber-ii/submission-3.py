class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # a simple solution. Create two different lists and find the max in that

        # n = len(nums)

        # if n == 1:
        #     return nums[0]

        # if n == 2:
        #     return 0

        # temp = [0]
        # for num in nums:
        #     temp.append(num)

        # nums = temp

        # dp1 = [0] * (n) # last is n-1
        # dp2 = [0] * (n+1) # last is n

        # dp1[1] = nums[1]
        # dp1[2] = max(nums[1], nums[2])

        # dp2[2] = nums[2]
        # dp2[3] = nums[3]

        # for i in range(3, n):
        #     dp1[i] = max(dp1[i], nums[i] + dp1[i-2])
        
        # for i in range(4, n+1):
        #     dp2[i] = max(dp2[i], nums[i] + dp2[i-2])

        # return max(dp1[n-1], dp2[n])

        def HR(h: List[int]):

            n = len(h)

            if n == 1:
                return h[0]
            if n == 2:
                return max(h[0], h[1])
            
            temp = [0]
            for num in h:
                temp.append(num)
            h = temp

            dp = [0] * (n + 1)
            dp[1] = h[1]
            dp[2] = max(h[1], h[2])
            
            for i in range(3, n+1):
                dp[i] = max(dp[i-1], dp[i-2] + h[i])

            return dp[n]

        n2 = len(nums)

        if n2 == 1:
            return nums[0]
        if n2 == 2:
            return (max(nums[0], nums[1]))

        return max(HR(nums[1:]), HR(nums[:n2-1]))