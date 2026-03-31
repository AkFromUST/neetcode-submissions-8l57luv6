class Solution:
    def find_cut(self, nums: List[int], target: int) -> int:

        # this is from the earlier neetcode question. Finding the deflection point is the same
        # as finding the min of the array

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2
    
            if nums[mid] < nums[mid - 1]:
                return mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

    def search(self, nums: List[int], target: int) -> int:

        # by the hints, simply find the deflection point. Once found. Perform binary search in the right sorted segment

        if not nums:
            return -1
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        cut = self.find_cut(nums, target)
        print(cut)
        
        l , r = 0, len(nums) - 1

        if cut == len(nums) - 1:
            if nums[-1] == target:
                return cut
            else:
                l = 0
                r = len(nums) - 1
        else:
            if nums[cut] <= target <= nums[len(nums)-1]:
                l = cut
            else:
                r = cut
        
        #now perform a simple bs

        while l <= r:

            mid = (l + r) // 2

            if (nums[mid] == target):
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            
        return -1



