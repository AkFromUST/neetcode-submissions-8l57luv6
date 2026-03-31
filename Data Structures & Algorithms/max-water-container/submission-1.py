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

        #return max(res)

        #optimizing

        i = 0
        j = len(res) - 1

        v_max = -1*float("inf")
        while (i < j):
            area = min(nums[i], nums[j]) * (j-i)

            v_max = max(v_max, area)

            if (nums[i] > nums[j]):
                j -= 1
            elif (nums[i] <= nums[j]):
                i += 1
        
        return v_max


