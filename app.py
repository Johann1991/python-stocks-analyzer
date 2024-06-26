from flask import Flask, render_template # type: ignore
import yfinance as yf # type: ignore
import pandas_ta as ta # type: ignore
import matplotlib.pyplot as plt # type: ignore
import io
import base64
import time
from utils.balance import get_account_balance
from utils.ohlcv import fetch_ohlcv
from utils.indicators import calculate_indicators
from utils.market_structure import identify_market_structure
from utils.liquidity_zones import identify_liquidity_zones
from utils.order_blocks import identify_order_blocks
from utils.supply_demand_zones import identify_supply_demand_zones
from utils.trading_signal import trading_signal
from utils.orders import place_order

app = Flask(__name__)

@app.route('/')
def index():
    # Define the stock ticker and the date range
    ticker = 'AAPL'
    start_date = '2024-07-01'
    end_date = '2025-07-31'
    
    # Download historical data for the specified stock and date range
    df = yf.download(ticker, start=start_date, end=end_date)
    
    # Calculate a 14-day Simple Moving Average (SMA)
    df['SMA_14'] = ta.sma(df['Close'], length=14)
    
    # Calculate the Relative Strength Index (RSI)
    df['RSI_14'] = ta.rsi(df['Close'], length=14)
    
    # Plot the closing price and the SMA
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(df['Close'], label='Close Price')
    ax.plot(df['SMA_14'], label='14-Day SMA', linestyle='--')
    ax.set_title(f'{ticker} Close Price and 14-Day SMA')
    ax.legend()
    
    # Save the plot to a bytes buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close(fig)
    
    # Plot the RSI
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(df['RSI_14'], label='14-Day RSI', color='purple')
    ax.axhline(70, linestyle='--', alpha=0.5, color='red')
    ax.axhline(30, linestyle='--', alpha=0.5, color='green')
    ax.set_title(f'{ticker} 14-Day RSI')
    ax.legend()
    
    # Save the plot to a bytes buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    rsi_url = base64.b64encode(img.getvalue()).decode()
    plt.close(fig)
    
    return render_template('index.html', plot_url=plot_url, rsi_url=rsi_url)

def trading_bot(symbol, amount):
    balance = get_account_balance()
    if 'error' in balance:
        print(f"Error fetching balance: {balance['message']}")
        return

    print(f"Account Balance: {balance}")

    df = fetch_ohlcv(symbol, '1d', 100)
    if 'error' in df:
        print(f"Error fetching market data: {df['message']}")
        return

    df = calculate_indicators(df)
    df = identify_market_structure(df)
    df = identify_liquidity_zones(df)
    df = identify_order_blocks(df)
    df = identify_supply_demand_zones(df)
    df = trading_signal(df)

    current_signal = df['signal'].iloc[-1]
    print(f"Current Signal: {current_signal}")

    if current_signal == 'buy':
        order_response = place_order(symbol, 'buy', amount)
        print(f"Buy Order Response: {order_response}")
    elif current_signal == 'sell':
        order_response = place_order(symbol, 'sell', amount)
        print(f"Sell Order Response: {order_response}")
    else:
        print("No trading action taken.")

if __name__ == '__main__':
    symbol = 'BTC/USD/Index'
    amount = 1  # Example amount, adjust according to your needs
    while True:
        trading_bot(symbol, amount)
        time.sleep(60)  # Run every 60 seconds, adjust the interval as needed

    app.run(debug=True, port=8080)
