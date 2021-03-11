import sqlite3

db = sqlite3.connect('data/stocks.db')
c = db.cursor()
c.execute('create table portfolio (symbol text, shares integer, price real)')
db.commit()

# stocks = [
#     ('GOOG', 100, 1093.05),
#     ('AAPL', 50, 217.68),
#     ('FB', 150, 155.42),
#     ('MSFT', 100, 109.03),
#     ('SNAP', 75, 6.88)
# ]
# c.executemany('insert into portfolio values (?,?,?)', stocks)
# db.commit()

# for row in db.execute('select * from portfolio'):
#     print(row)


# min_price = 150

# print('\nExpensive Stocks:')
# for row in db.execute('select * from portfolio where price > ?',
#                       (min_price,)):
#     print(row)
