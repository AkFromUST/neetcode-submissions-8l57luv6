class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if (len(nums) == 1):
            return nums[0]
        
        
        #kadane's Algorithm
        v = []
        for i in range(len(nums)):
            v.append(0)

        v[0] = nums[0] 

        v_max = v[0]

        for i in range(1, len(nums)):
            v[i] = v[i-1] + nums[i]
        
            v[i] = max(v[i], nums[i])
        
            v_max = max(v[i], v_max)

        return v_max