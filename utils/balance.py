import requests # type: ignore

api_token = '84JRhutlTMKHALm'
base_url = 'https://api.deriv.com'

headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json',
}

def get_account_balance():
    endpoint = f'{base_url}/v3/balance'
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': response.status_code, 'message': response.text}
