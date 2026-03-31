class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        w = []

        for i in range(len(nums)):
            w.append(0)

        #base case
        w[0] = nums[0]
        w[1] = max(nums[0], nums[1])

        for i in range(2,len(nums)):
            w[i] = max(nums[i] + w[i-2], w[i-1])
        
        return w[len(nums)-1]