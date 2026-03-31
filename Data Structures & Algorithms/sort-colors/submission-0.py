class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        temp = {0: 0, 1: 0, 2: 0}

        for i in range(n):
            temp[nums[i]] += 1

        l = 0
        for i in range(3):
            for k in range(temp[i]):
                nums[l] = i
                l += 1

        return nums