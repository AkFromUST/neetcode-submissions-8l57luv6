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
        

    def pop(self) -> int:
    
        highestfreq = 1
        potentials = []
        for e, f in self.counter.items():
            if f > highestfreq:
                highestfreq = f

        potentials = set()
        #get the key(s) with this values
        for ele, freq in self.counter.items():
            if freq == highestfreq:
                potentials.add(ele)

        #now check which one is the nearest
        put_back = []

        removed = -1
        for i in range(len(self.stack)):
            removed = self.stack.pop()
            if removed not in potentials:
                put_back.append(removed)
            else:
                break
        
        self.counter[removed] -= 1
        if self.counter[removed] == 0:
            del self.counter[removed]

        #put it back
        for r in range(len(put_back)):
            self.stack.append(put_back.pop())
        
        return removed
        
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()