stock_prices = {
    "AAPL":180,
    "TSLA":250,
    "GOOG":140,
    "AMZN":130
}
print("Stock Portfolio Tracker")
total_investment = 0
n = int(input("How many stocks do you want to add? "))

for i in range(n): 
    print("\nStock", i+1)
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        price = stock_prices[stock_name]
        total = price * quantity
        total_investment += total

        print("Price:", price)
        print("Total:", total)
    else:
        print("Stock not found")
print("\nTotal Investment =", total_investment)

  