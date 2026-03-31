class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # #implemented on july-14
        # #this is brute force. The Time complexity is dominated by the sorting -> O(nlog(n))
        
        # if (k == len(nums)):
        #     return nums

        # counterMap = {}
        # resMap = defaultdict(list)
        # for num in nums:
        #     counterMap[num] = 1 + counterMap.get(num, 0)

        # for key, value in counterMap.items():
        #     resMap[value].append(key)

        # freqList = list(resMap.keys())
        # freqList.sort(reverse=True)
        # res = []
        # counter = 0
        # for key in freqList:
        #     for num in resMap[key]:
        #         if (len(res) < k):
        #             res.append(num)
        #             counter += 1
        # return res

        
        #For the sorting bottleneck. we have a workaround
        # freq: i is the freq and freq[i] is the number with that frequency
        freq_list = []
        for i in range(10001):
            freq_list.append([])

        counterMap, freqMap = {}, defaultdict(list)
        for num in nums:
            counterMap[num] = 1 + counterMap.get(num, 0)
        
        for num, freq in counterMap.items():
            freqMap[freq].append(num)

        # print(freqMap)

        #now freq[index] represents the number that has index frequency
        for freqs in list(freqMap.keys()):
            for num in freqMap[freqs]:
                freq_list[freqs].append(num)

        # print(freq_list[:100])

        #reverse iterate to freq and stop when you reach k elements
        k_count = 0
        res = []
        for i in range(len(freq_list)-1,-1,-1):
            if (freq_list[i] != []):
                for num in freq_list[i]:
                    res.append(num)
        return res[:k]

        
