def add_stock(portfolio, ticker, shares, price):
    for stock in portfolio:
        if stock['ticker'] == ticker:
            stock['shares'] += shares
            stock['price'] = price
            return
    
    new_stock = {'ticker': ticker, 'shares': shares, 'price': price}
    portfolio.append(new_stock)

def view_portfolio(portfolio):
    print("Portfolio:")
    for stock in portfolio:
        ticker = stock['ticker']
        shares = stock['shares']
        price = stock['price']
        print(f"{ticker}: {shares} shares at ${price:.2f} each")

def calculate_total_value(portfolio):
    total_value = 0.0
    for stock in portfolio:
        total_value += stock['shares'] * stock['price']
    return total_value

def main():
    portfolio = []
    
    while True:
        print("\nStock Portfolio Management")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Calculate Total Value")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            ticker = input("Enter stock ticker: ")
            shares = int(input("Enter number of shares: "))
            price = float(input("Enter price per share: "))
            add_stock(portfolio, ticker, shares, price)
            print(f"Stock {ticker} added/updated.")
        
        elif choice == '2':
            view_portfolio(portfolio)
        
        elif choice == '3':
            total_value = calculate_total_value(portfolio)
            print(f"Total portfolio value: ${total_value:.2f}")
        
        elif choice == '4':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

main()