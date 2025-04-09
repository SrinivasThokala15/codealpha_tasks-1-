import yfinance as yf
import pandas as pd

def get_stock_price(ticker):
    """Fetch the latest stock price for a given ticker symbol."""
    stock = yf.Ticker(ticker)
    return stock.history(period='1d')['Close'].iloc[-1]

def update_portfolio(portfolio):
    """Update portfolio with the latest stock prices."""
    for stock in portfolio:
        stock['Current Price'] = get_stock_price(stock['Ticker'])
        stock['Total Value'] = stock['Shares'] * stock['Current Price']
    return portfolio

def display_portfolio(portfolio):
    """Display the portfolio in a table format."""
    df = pd.DataFrame(portfolio)
    print(df)
    print(f"Total Portfolio Value: ${df['Total Value'].sum():,.2f}")

# Example Portfolio
portfolio = [
    {'Ticker': 'AAPL', 'Shares': 10, 'Current Price': 0, 'Total Value': 0},
    {'Ticker': 'GOOGL', 'Shares': 5, 'Current Price': 0, 'Total Value': 0},
    {'Ticker': 'TSLA', 'Shares': 8, 'Current Price': 0, 'Total Value': 0}
]

# Update and display portfolio
portfolio = update_portfolio(portfolio)
display_portfolio(portfolio)