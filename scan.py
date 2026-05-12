import yfinance as yf

stocks = ['SPY', 'AAPL', 'MSFT', 'NVDA', 'GOOGL', 'TSLA']

print("Stock Prices:")
print("-" * 30)

for stock in stocks:
    try:
        ticker = yf.Ticker(stock)
        price = ticker.info.get('regularMarketPrice', 0)
        print(f"{stock}: ${price}")
    except:
        print(f"{stock}: error")
