class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        """
        #The brute force approach

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
        """

        res = []

        #key stores the element and value is the LIS starting from that element
        hashmap = {}

        def dfs(i, prev):

            if i == len(nums):
                return 0

            #checking for the memoisation
            if (prev, i) in hashmap:
                return hashmap[(prev, i)]

            #dont take
            temp2 = dfs(i+1, prev)
            
            temp = 0
            #take if curr element is larger than prev taken
            if prev == -1 or (nums[prev] < nums[i]):
                temp = 1 + dfs(i+1, i)

            #memoisation all the way
            hashmap[(prev, i)] = max(temp, temp2)
            return hashmap[(prev, i)]

        return dfs(0, -1)

        """
        #bottom up dp approach

        n = len(nums)
        dp = [1] * n

        prev = nums[n-1]

        for i in range(n-2, -1, -1):
            if nums[i] < prev:
                dp[i] += dp[i+1]
                prev = nums[i]
            else:
                dp[i] = dp[i+1]
        return dp[0]
        """