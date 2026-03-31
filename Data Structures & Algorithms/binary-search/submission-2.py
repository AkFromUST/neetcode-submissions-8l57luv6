class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #Simple binary Search
        prev_values = set()
        def BS(start, end):
            
            if (start > end):
                return -1

            index = int((start + end)/2)

            if (nums[index] == target):
                return index

            if (nums[index] > target):
                return BS(start, index-1)
            else:
                return BS(index+1, len(nums)-1)

        #I like to start at the middle
        return BS(0,len(nums)-1)