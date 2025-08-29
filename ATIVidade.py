import requests
import pandas as pd

# -------------------------------
# Função para coletar os dados da API Olinda
# -------------------------------
def coletar_dados_odata(url, parametro_data):
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados_json = resposta.json()
    registros = dados_json["value"]

    df = pd.DataFrame(registros)

    # Criar coluna da data de referência
    df["DataReferencia"] = parametro_data  
    df["DataReferencia"] = pd.to_datetime(df["DataReferencia"])

    return df


# -------------------------------
# URLs base da API
# -------------------------------
urls = {
    "chavespix": "https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/ChavesPix(Data=@Data)?@Data='{data}'&$top=100&$format=json",
    "estatisticas": "https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/EstatisticasTransacoesPix(Database=@Database)?@Database='{data}'&$top=100&$format=json",
    "transacoes_municipio": "https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/TransacoesPixPorMunicipio(DataBase=@DataBase)?@DataBase='{data}'&$top=100&$format=json"
}

# -------------------------------
# Anos que vamos percorrer
# -------------------------------
anos = ["2023-01-01", "2024-01-01", "2025-01-01"]

# -------------------------------
# Coleta e junta os dados
# -------------------------------
for nome, url in urls.items():
    lista_dfs = []  # acumula os dataframes de cada ano

    for ano in anos:
        url_formatada = url.format(data=ano)
        print(f" Coletando {nome} para {ano}...")
        df = coletar_dados_odata(url_formatada, ano)
        lista_dfs.append(df)

    # Concatenar todos os anos
    df_final = pd.concat(lista_dfs, ignore_index=True)

    # Salvar em um único CSV
    nome_arquivo = f"{nome}_todos.csv"
    df_final.to_csv(nome_arquivo, index=False, encoding="utf-8-sig")

    print(f" Salvo: {nome_arquivo}")

print("\n Finalizado! Gerados 3 arquivos consolidados.")
