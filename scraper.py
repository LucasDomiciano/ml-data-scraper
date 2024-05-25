import requests

def obter_dados_mercado_livre(token):
    url = 'https://api.mercadolibre.com/sites/MLB/search?category=MLB1403&limit=50'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception('Erro ao obter dados: ' + response.text)
    
    data = response.json()
    
    # Adicionando depuração para verificar a estrutura da resposta
    print("Resposta da API:", data)
    
    if 'results' not in data or len(data['results']) == 0:
        raise Exception('Nenhum dado encontrado')
    
    produtos = []
    for item in data['results']:
        produto = {
            'Título': item['title'],
            'Preço': item['price'],
            'Vendedor': item['seller']['id'],
            'Link': item['permalink'],
            'Vendidos': item.get('sold_quantity', 0)  # Usando get com valor padrão 0
        }
        produtos.append(produto)
    
    return produtos