class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        state = 0
        best = 100001
        n = len(nums)
        
        for i in range(n):
            #window is not even upto target
            state += nums[i]

            #check if we can shorten it up?
            while state >= target:
                best = min(best, (i - l + 1))
                state -= nums[l]
                l += 1

        if best >= 100001:
            return 0
        return best