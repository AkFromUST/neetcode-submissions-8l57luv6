class Solution:
    def countOdds(self, low: int, high: int) -> int:
        first = 0
        for i in range(low, high+1):
            if (i % 2) != 0:
                first = i
                break
        last = 0
        for i in range(high, low-1, -1):
            if (i % 2) == 1:
                last = i
                break
        
        if first == last:
            if first % 2 != 0:
                return 1
            return 0
        return (last -first + 1) // 2 + 1