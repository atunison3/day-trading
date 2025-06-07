from datetime import datetime 

class Transaction:
    def __init__(self, transaction_id: int, ticker: str, date: datetime, quantity: int, price: float, buy: bool):
        self.transaction_id = transaction_id 
        self.ticker = ticker 
        self.date = date 
        self.quantity = quantity 
        self.price = price 
        self.buy = buy 

    @property
    def insert_data(self) -> tuple:
        return self.ticker, self.date, self.quantity, self.price, self.buy 