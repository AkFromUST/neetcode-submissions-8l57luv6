class Solution:
    def numDecodings(self, s: str) -> int:
        """
        #can we break down into all possible substrings and check which ones are valid and which ones are not?

        #dp relation <- +1 only if the i,i-1 is within the right range
        if s[0] == "0":
            return 0
        
        s = "0" + s
        n = len(s)
        dp = [0] * n
        print(s)

        if s[n-1] != "0":
            dp[n-1] = 1

        i = n-1

        while i >= 1:
            print("\tCurrent element: ", s[i], "with index: ", i)
            if i == n-1:
                if s[i] != "0":
                    dp[i] = 1
            else:
                dp[i] = dp[i+1]

            #if the current is 0 then
            if s[i] == "0":
                #check if the two can be grouped together or not
                temp = int(s[i-1] + s[i])
                print("s[i]: ", s[i], "\t\ttemp: ", temp, "\t\ti: ", i)
                #locking these in
                if 10 <= temp <= 26:
                    dp[i-1] = dp[i]
                    i -= 2
                    print("s[i-1]: ", s[i-1], "\t\ti: ", i, "\t\ts[i-2]: ", s[i-2], "\t\tdp[i-1]: ", dp[i-1])
                    continue

            else:
                if s[i-1] != "0":
                    temp = int(s[i-1] + s[i])
                    if 10 <= temp <= 26:
                        dp[i] += 1

            i -= 1

        print(dp)
        return dp[1]
        """

        #from the hints, there is a brute force that we can explore

        total = 0
       
        def dfs(i):

            if i >= len(s):
                return 1

            #if the current is a zero?
            if s[i] == "0":
                #cant use this current index to form anything. Move on
                return 0

            res = dfs(i + 1)
            
            #suppose the current is not a zero and combining the next digit also gives us valid decoding ways
            if (i <= len(s) - 2) and (10 <= int(s[i] + s[i+1]) <= 26) and (s[i] != "0"):
                res += dfs(i + 2)

            return res

        return dfs(0)





















































        
