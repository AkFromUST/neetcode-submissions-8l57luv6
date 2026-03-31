class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        res = 0
        maxw = -1
        for num in self.stack:
            if num <= price:
                res += 1
            else:
                res = max(res, maxw)
                res = 0
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)