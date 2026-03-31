class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        
        for k,v in hashmap.items():
            if v > 1:
                return k