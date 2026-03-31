class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if (k == len(nums)):
            return nums

        counterMap = {}
        resMap = defaultdict(list)
        for num in nums:
            counterMap[num] = 1 + counterMap.get(num, 0)

        for key, value in counterMap.items():
            resMap[value].append(key)

        freqList = list(resMap.keys())
        freqList.sort(reverse=True)
        res = []
        counter = 0
        for key in freqList:
            for num in resMap[key]:
                if (len(res) < k):
                    res.append(num)
                    counter += 1
        return res