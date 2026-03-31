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

        #asked perplexity for help. The code is perplexity but my logic was correct
        #my mistake was on returning part. I was not summing up the different possibilities from different branches, thus undercounting

        dp = {len(s) : 1}

        def backtracking(i):
            
            if i in dp:
                return dp[i]

            if s[i] == "0":
                return 0


            #at this point, its a 1
            #we dont return cuz we want all branches to sum up
                #tried the nonlocal var but for some reason it didnt work
            res = backtracking(i + 1)

            if s[i] != "0":
                #check if there is a pair
                if (i <= len(s) - 2 and (10 <= int(s[i] + s[i+1]) <= 26)):
                    res += backtracking(i + 2)
            dp[i] = res
            return res

        return backtracking(0)


        #converting this to dp