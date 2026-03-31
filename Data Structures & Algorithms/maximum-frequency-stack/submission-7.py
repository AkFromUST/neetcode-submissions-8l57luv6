class FreqStack:

    def __init__(self):
        from collections import heapq

        self.counter = {}
        self.maxheap = []

    def push(self, val: int) -> None:

        if val not in self.counter:
            self.counter[val] = 1
        else:
            self.counter[val] += 1

        #now get the counter val
        freq = self.counter[val]

        #now check the max_heap

        if not self.maxheap:
            heapq.heappush(self.maxheap, [-1 *freq, [val]])
            return None

        for f, ele_list in self.maxheap:
            if (-1 * freq) == f:
                ele_list.append(val)
                return None
        
        #else this is a new freq
        heapq.heappush(self.maxheap, [-1 * freq, [val]])
        

    def pop(self) -> int:

        #get the highest freq
        freq, element_list = heapq.heappop(self.maxheap)

        #get the latest element
        res = element_list.pop()

        self.counter[res] -= 1

        if element_list:
            heapq.heappush(self.maxheap, [freq, element_list])

        return res
        
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()