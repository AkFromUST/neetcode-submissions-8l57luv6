class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def backtracking(index, currT, subs):
            
            #memoisation advantage
            if (currT, tuple(subs)) in memo:
                return memo[(currT, tuple(subs))]

            #end case
            if currT == 0:
                #check the subs
                freq = {}

                for num in subs:
                    if num not in freq:
                        freq[num] = 1
                    else:
                        freq[num] += 1
                
                #denominator factorial
                den = 1
                for key, val in freq.items():
                    #factorial
                    for i in range(1, val + 1):
                        den *= i
                
                #numerator factorial
                n = len(subs)

                num = 1
                for i in range(1, n+1):
                    num *= i
                ans = num / den

                return int(ans)

            if currT < 0 or index >= len(nums):
                return 0
 
            #dont take
            dtake = backtracking(index + 1, currT, subs)

            #take
            subs.append(nums[index])
            take = backtracking(index, currT - nums[index], subs)
            subs.pop()

            memo[(currT, tuple(subs))] = dtake + take
            
            return dtake + take

        return backtracking(0, target, [])