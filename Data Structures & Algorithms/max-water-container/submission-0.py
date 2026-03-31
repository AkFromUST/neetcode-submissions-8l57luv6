class Solution:
    def maxArea(self, nums: List[int]) -> int:
        
        #brute force
        res = []

        for i in range(len(nums)):
            v_max = -1*float("inf")
            for j in range(i+1, len(nums)):
                x = min(nums[j], nums[i])
                area = x * (j-i)  
                v_max = max(v_max, area)
            res.append(v_max)

        return max(res)
