class Portfolios(object):
    def __init__(self):
        self.holdings = {}

    def buy(self, tickers, shares):
        self.holdings[tickers] = self.holdings.get(tickers, 0) + shares

    def seller(self, tickers, shares):
        self.holdings[tickers] = self.holdings.get(tickers, 0) - shares

    def __iter__(self):
        return iter(self.holdings.items())


p = Portfolios()
p.buy('A',10)
p.buy('A',20)
p.buy('A',30)
p.buy('B',10)
p.seller('A',10)

for key,value in p:
    print(key,value)