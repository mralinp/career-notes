import itertools

def iterator_usage():
    usernames = ('ali', 'mamad', 'ahmad', 'ehsan')

    loop_1 = usernames.__iter__()
    print(loop_1.__next__())
    print(loop_1.__next__())
    print(loop_1.__next__())
    print(loop_1.__next__())

    # print(loop_1.__next__()) # raises StopIteration exception

    loop_2 = iter(usernames)

    print(next(loop_2))
    print(next(loop_2))
    print(next(loop_2))
    print(next(loop_2))
    # print(next(loop_2)) # raises StopIteration exception

    loop_3 = iter(usernames)

    while True:
        try:
            user = next(loop_3)
            print(user)
        except StopIteration:
            break
    
def iterator_in_classes():
    class Portfolio:
        
        def __init__(self):
            self.holdings = {}
        
        def buy(self, ticker, shares):
            self.holdings[ticker] = self.holdings.get(ticker, 0) + shares
        
        def sell(self, ticker, shares):
            self.holdings[ticker] = self.holdings.get(ticker, 0) - shares
        
        def __iter__(self):
            return iter(self.holdings.items())
        

    p = Portfolio()
    p.buy("alpha", 15)
    p.buy("beta", 23)
    p.buy("gamma", 9)
    p.buy("gamma", 20)

    for (ticker, shares) in p:
        print(ticker, shares)
        
def product_cards():
    ranks = list(range(2,11)) + ['J', 'Q', 'K', 'A']
    ranks = [str(rank) for rank in ranks]
    
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    deck = [card for card in itertools.product(ranks, suits)]
    
    for index, card in enumerate(deck):
        print(index + 1, card)
        
    hands = [hand for hand in itertools.combinations(deck, 5)]
    print(f"The number of 5-card poker hands is {len(hands)}.")

if __name__ == '__main__':
    
    product_cards()