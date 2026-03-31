class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        LIS = []
        for i in range(len(nums)):
            LIS.append(1)

        #base case
        LIS[len(nums) - 1] = 1

        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if (nums[i] < nums[j]):
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)
            

