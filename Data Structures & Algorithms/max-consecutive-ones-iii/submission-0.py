class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l, maxlen, currz = 0,0,0
        n = len(nums)

        for i in range(n):
            
            if nums[i] == 0:
                currz += 1
            
            while currz > k:
                #keep moving the left guy
                if nums[l] == 0:
                    currz -= 1
                l += 1
            
            maxlen = max(maxlen, i - l + 1)

        return maxlen