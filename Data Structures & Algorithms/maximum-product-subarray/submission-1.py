class Solution:
    def maxProduct(self, nums: List[int]) -> int:
                
        if (len(nums) == 1):
            return nums[0]


        v_max = []
        for i in range(len(nums)):
            v_max.append(-2*float("inf"))

        v_max[0] = nums[0]

        temp = v_max[0]
        for i in range(1, len(nums)):
            temp *= nums[i]
            v_max[i] = max(v_max[i-1], temp, nums[i])

        return v_max[len(nums)-1]