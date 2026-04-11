class StockSpanner:

    def __init__(self):
        self.stockspan = []

    def next(self, price: int) -> int:
        tempstockspan = []
        span = 1
        while self.stockspan and self.stockspan[-1] <= price:
            tempstockspan.append(self.stockspan.pop())
            span += 1
        else:
            while tempstockspan:
                self.stockspan.append(tempstockspan.pop())
            self.stockspan.append(price)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)