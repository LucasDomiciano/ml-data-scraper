from auth import obter_token
from scraper import obter_dados_mercado_livre
from exporter import exportar_para_excel

def main():
    # Substitua pelos valores reais
    client_id = 'CLIENT_API'
    client_secret = 'client_id'
    redirect_uri = 'redirect_uri'
    code = 'code'
    
    try:
        token = obter_token(client_id, client_secret, redirect_uri, code)
        produtos = obter_dados_mercado_livre(token)
        exportar_para_excel(produtos)
        print("Dados exportados com sucesso para 'produtos_mercado_livre.xlsx'.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
