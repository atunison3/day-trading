import sqlite3 

from domain.transaction import Transaction

class SqliteRespository:

    def __init__(self, repository: str):
        self.repository = repository 

    def _connect(self) -> sqlite3.cursor:
        '''Connects to the repository'''

        self.conn = sqlite3.connect(self.repository)
        cursor = conn.cursor() 

        return cursor

    def _disconnect(self) -> None:
        '''Disconnects from the repository'''

        self.conn.commit()
        self.conn.close()
    
    def create_transaction(self, t: Transaction) -> None:
        '''Insert a transaction'''

        cursor = self._connect() 
        sql = 'INSERT INTO transactions (ticker, date, quantity, price, buy) VALUES (?, ?, ?, ?, ?);'
        cursor.execute(sql, t.insert_data)
        self._disconnect()

    def read_all_transactions(self) -> list[Transaction]:
        '''Read all transactions'''

        cursor = self._connect()
        sql = 'SELECT * FROM transactions;'
        results = cursor.fetchall()
        self._disconnect()

        transactions = []
        for result in results:
            transactions.append(Transaction(
                result[0], 
                result[1], 
                result[2], 
                result[3], 
                result[4], 
                result[5]
            ))

        return transactions

    def read_transaction_by_id(self, transaction_id: int) -> Transaction:
        '''Read a given transaction by id'''

        cursor = self.connect() 
        sql = 'SELECT * FROM transactions WHERE transaction_id = ?;'
        cursor.execute(sql, (transaction_id,))
        result = cursor.fetchone() 
        self._disconnect()

        if result:
            return Transaction(
                result[0], 
                result[1], 
                result[2], 
                result[3], 
                result[4], 
                result[5]
            )
        else:
            return None

