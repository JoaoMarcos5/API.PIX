import requests
import pandas as pd


def consultar_dados_pix(url, ano="2023-01-01"):
    """
    Consulta a API do BCB e retorna um DataFrame com os dados do ano informado.
    """
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        dados_json = resp.json()
        registros = dados_json.get("value", [])
        
        if not registros:
            print(f"Atenção: Nenhum dado encontrado para {ano} na URL {url}")
            return pd.DataFrame()
        
        df = pd.DataFrame(registros)
        # Adiciona coluna de referência de data
        df["DataReferencia"] = pd.to_datetime(ano)
        return df
    except Exception as e:
        print(f"Erro ao consultar dados: {e}")
        return pd.DataFrame()


# -------------------------------
# URLs para 2023
# -------------------------------
urls_2023 = {
    "chavespix": "https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/ChavesPix(Data=@Data)?@Data='2023-01-01'&$top=100&$format=json",
    "estatisticas": "https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/EstatisticasTransacoesPix(Database=@Database)?@Database='2023-01-01'&$top=100&$format=json",
    "transacoes_municipio": "https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/TransacoesPixPorMunicipio(DataBase=@DataBase)?@DataBase='2023-01-01'&$top=100&$format=json"
}

# -------------------------------
# Consultar e armazenar em memória
# -------------------------------
dados = {}

for nome, url in urls_2023.items():
    print(f"Consultando {nome} para 2023...")
    df = consultar_dados_pix(url, ano="2023-01-01")
    dados[nome] = df  # salva no dicionário

# -------------------------------
# Exemplo de consulta no Python
# -------------------------------
print("\n--- Chaves Pix 2023 ---")
print(dados["chavespix"].head())

print("\n--- Estatísticas 2023 ---")
print(dados["estatisticas"].head())

print("\n--- Transações por Município 2023 ---")
print(dados["transacoes_municipio"].head())
