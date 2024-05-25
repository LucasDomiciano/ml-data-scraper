import requests

def obter_token(client_id, client_secret, redirect_uri, code):
    url = 'https://api.mercadolibre.com/oauth/token'
    payload = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'code': code
    }
    
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        raise Exception('Erro ao obter token: ' + response.text)
