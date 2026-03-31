class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = []

        for i in range(20001):
            counter.append(0)
    
        for i in range(len(nums)):
            if (nums[i] < 0):
                counter[abs(nums[i]) + 10000] += 1
            else:
                counter[nums[i]] += 1

        res = []
        for i in range(k):
            max_index = counter.index(max(counter))

            if (max_index <= 10000):
                res.append(max_index)
                counter[max_index] = 0
            else:
                x = max_index - 10000
                res.append(-1*x)
                counter[max_index] = 0

        return res