import pandas as pd

def exportar_para_excel(produtos, nome_arquivo='produtos_mercado_livre.xlsx'):
    df = pd.DataFrame(produtos)
    df.to_excel(nome_arquivo, index=False)
