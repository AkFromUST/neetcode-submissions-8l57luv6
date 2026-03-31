class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if (not nums):
            return 0

        v_min = float("inf")
        v_max = -1 * float("inf")
        
        hashmap = {}

        v_min = min(nums)
        v_max = max(nums)

        for i in range(v_min, v_max+1):
            if (i in nums):
                hashmap[i] = 1
            else:
                hashmap[i] = 0
        
        res_max = -1*float("inf")
        res = 0

        for i in range(v_min, v_max+1):
            if (hashmap[i] == 0):
                res = 0
            else:
                res += 1
            res_max = max(res_max, res)

        return res_max
            

