# stocks.py

# PART 1 Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.

# PART 2 Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.



stockDict = {
'GE': 'General Electric',
'CAT':'Caterpillar',
'EK':'Eastman Kodak'
}


purchases = [
( 'GE', 100, '10-sep-2001', 48 ),
( 'CAT', 100, '1-apr-1999', 24 ),
( 'GE', 200, '1-jul-1998', 56 )
]

portfolio = dict()

# ---------- PART 1

for purchase in purchases:
    ticker = purchase[0]

    full_company_name = stockDict[ticker]
    number_of_shares = purchase[1]
    purchase_price = purchase[3]
    full_purchase_price = number_of_shares * purchase_price


# ---------- PART 2
    try:
        portfolio[ticker].append(purchase)
    except KeyError:
        portfolio[ticker] = list()
        portfolio[ticker].append(purchase)

    print("I purchased {0} stock for ${1}\n\n".format(full_company_name, full_purchase_price))

for key, values in portfolio.items():
    for value in values:
        for i in value:
            print(i)

    print(ticker)
    total_portfolio_stock_value = 0
    for purchase in purchases:
        total_portfolio_stock_value += purchase[1] * purchase[3]
        print(purchase)
    print("Total value of stock in portfolio: ${}\n\n".format(total_portfolio_stock_value))

something = tuple()
something_else = list()
something_else.append("Cool things")
something_else.append("awesome")
if "Cool things" in something_else:
    print("Meg is cool")
print(something_else)
tuple(something_else)
# print(dir(something_else))



















