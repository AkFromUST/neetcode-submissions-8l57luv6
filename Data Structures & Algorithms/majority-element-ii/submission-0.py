class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count_hashmap = {}

        for i in range(len(nums)):
            if nums[i] not in count_hashmap:
                count_hashmap[nums[i]] = 1
            else:
                count_hashmap[nums[i]] += 1

        target = int(len(nums)/3)
        res = []
        for element, freq in count_hashmap.items():
            if freq > target:
                res.append(element)
        
        return res