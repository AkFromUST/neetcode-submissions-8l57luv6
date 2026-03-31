class Solution:
    def findMin(self, nums: List[int]) -> int:

        #intuition -> 
            # keep the prev_mid in mind. If the prev_mid is higher than the current mid, you are in the right window
            # else, just keep going right
            # by the end of it, if you dont see anything in the right, then the array is already sorted and just return nums[0]

        #edge case 1
        if len(nums) == 1:
            return nums[0]

        #potential edge case 2
        if not nums:
            return 0

        l = 0
        r = len(nums)- 1

        #if rotated n times, just return the first element
        if (nums[r] > nums[l]):
            return nums[0]

        while l <= r:

            mid = (l + r) // 2

            print("\tnew mid: ", nums[mid], "\tl: ", l, "\tr: ", r)
    
            if (mid > 0) and (nums[mid - 1] > nums[mid]):
                return nums[mid]

            if (mid < len(nums) - 1) and (nums[mid+ 1] < nums[mid]):
                return nums[mid + 1]

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    






