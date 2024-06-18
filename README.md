# Stock Analysis with Flask

This project is a simple web application that performs stock analysis using historical data. It fetches data from Yahoo Finance, calculates technical indicators, and displays the results on an HTML page using Flask.

## Features

- Fetch historical stock data from Yahoo Finance
- Calculate technical indicators such as Simple Moving Average (SMA) and Relative Strength Index (RSI)
- Display the stock data and indicators in interactive plots on a web page

## Technologies Used

- Python
- Flask
- pandas
- pandas-ta
- yfinance
- matplotlib

## Installation

### Prerequisites

- Python 3.7+
- Git

### Steps

1. **Clone the repository**

   git clone https://github.com/yourusername/stock-analysis.git
   cd stock-analysis

2. **Create and activate a virtual environment**

   #### Windows

   python -m venv venv
   venv\Scripts\activate

   #### macOS/Linux
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. **Open your browser and visit**

   ```
   http://127.0.0.1:8080/
   ```

## Project Structure

```bash
stock-analysis/
├── venv/                   # Virtual environment
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
└── templates/
    └── index.html          # HTML template
```

## How It Works

- The application uses the `yfinance` library to fetch historical stock data.
- It calculates the 14-day Simple Moving Average (SMA) and the 14-day Relative Strength Index (RSI) using `pandas-ta`.
- The data is plotted using `matplotlib` and displayed on a web page using Flask.
- The plots are rendered as images and embedded in the HTML template.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [pandas](https://pandas.pydata.org/)
- [pandas-ta](https://github.com/twopirllc/pandas-ta)
- [yfinance](https://pypi.org/project/yfinance/)
- [matplotlib](https://matplotlib.org/)
```