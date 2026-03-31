class Solution:

    def bs(self, l,r,nums,target) -> int:
        if l > r:
            return -1

        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.bs(l, mid - 1, nums, target)
        else:
            return self.bs(mid+1, r, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.bs(0,len(nums) - 1, nums, target)