class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        dp = [0] * (n+1)
        dp[n]=1
        if (s[n-1] != "0"):
            dp[n-1] = 1
            

        for i in range(n-2, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            if 1 <= int(s[i] + s[i+1]) <= 26 and i+2<n+1:
                dp[i] += dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]
        
        return dp[0]