import requests # type: ignore
import json

api_token = '84JRhutlTMKHALm'
base_url = 'https://api.deriv.com'

headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json',
}

def place_order(symbol, action, amount):
    endpoint = f'{base_url}/v3/order'
    order_data = {
        'symbol': symbol,
        'action': action,  # 'buy' or 'sell'
        'amount': amount,
    }
    response = requests.post(endpoint, headers=headers, data=json.dumps(order_data))
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': response.status_code, 'message': response.text}
