class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = []
        for i in range(len(nums)):
            for j in range(len(duplicates)):
                if (nums[i] == nums[j]):
                    return True
            duplicates.append(nums[i])
        return False