import requests # type: ignore
import pandas as pd # type: ignore

api_token = '84JRhutlTMKHALm'
base_url = 'https://api.deriv.com'

headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json',
}

def fetch_ohlcv(symbol, timeframe, limit):
    endpoint = f'{base_url}/v3/ohlcv?symbol={symbol}&timeframe={timeframe}&limit={limit}'
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['ohlcv'], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    else:
        return {'error': response.status_code, 'message': response.text}
