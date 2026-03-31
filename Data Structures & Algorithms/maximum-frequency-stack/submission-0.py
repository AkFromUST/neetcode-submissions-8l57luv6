class FreqStack:

    def __init__(self):
        from collections import heapq

        self.stack = []
        self.maxheap = []
        self.counter = {}

    def push(self, val: int) -> None:
        self.stack.append(val)

        if val not in self.counter:
            self.counter[val] = 1
        else:
            self.counter[val] += 1
        
        # if not self.maxheap:
        #     heapq.heappush(self.maxheap, [-1, val])
        #     return None
        
        # #otherwise we first find this item in the heap
        # added = False
        # for i in range(len(self.maxheap)):
        #     freq, element = self.maxheap[i][0], self.maxheap[i][1]
        #     if element == val:
        #         #update
        #         self.maxheap[i][0] -= 1
        #         heapq.heapify(self.maxheap)
        #         added = True
        #         break

        # if not added:
        #     heapq.heappush(self.maxheap, [-1, val])


    def pop(self) -> int:
        
        # #first get the element that is most freq
        # freq, element = heapq.heappop(self.maxheap)
        # freq += 1
        # heapq.heappush(self.maxheap, [freq, element])

        # put_back = []
        # for i in range(len(self.stack)-1, -1, -1):
        #     res = self.stack.pop()
        #     if res != element:
        #         put_back.append(res)
        #     else:
        #         break

        # for ele in put_back:
        #     self.stack.append(ele)

        # return element
        print("-"*10)
        print("Stack at the start: ", self.stack)
        highestfreq = 1
        potentials = []
        for ele, freq in self.counter.items():
            if freq > highestfreq:
                highestfreq = freq

        potentials = set()
        #get the key(s) with this values
        for ele, freq in self.counter.items():
            if freq == highestfreq:
                potentials.add(ele)

        #now check which one is the nearest
        put_back = []

        print("potentials: ", potentials)

        removed = -1
        for i in range(len(self.stack)):
            removed = self.stack.pop()
            if removed not in potentials:
                put_back.append(removed)
            else:
                break


        print("Counter: ", self.counter)
        print("removed: ", removed)
   

        self.counter[removed] -= 1
        if self.counter[removed] == 0:
            del self.counter[removed]

        #put it back
        for ele in put_back:
            self.stack.append(ele)
        
        print("Stack: ", self.stack)
        print("#"*10)
        
        return removed
        
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()