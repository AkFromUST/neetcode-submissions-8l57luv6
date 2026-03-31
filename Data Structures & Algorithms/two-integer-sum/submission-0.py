class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = 0
        for i in range(len(nums)):
            j = i + 1
            s = 0
            while (j < len(nums)):
                s = nums[i] + nums[j]
                if s == target:
                    return [i,j]
                j += 1

