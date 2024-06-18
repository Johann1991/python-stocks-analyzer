from flask import Flask, render_template
import yfinance as yf
import pandas_ta as ta
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # Define the stock ticker and the date range
    ticker = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2022-01-01'
    
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

if __name__ == "__main__":
    app.run(debug=True, port=8080)
