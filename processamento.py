import pandas as pd
from datetime import dadtetime

def carregar_planilha(caminho_arquivo):
    # Lê a planilha pulando as primeiras 6 linhas
    df = pd.read_excel(caminho_arquivo, skiprows=6)

    # Remove possíveis espaços invisíveis nos nomes das colunas
    df.columns = df.columns.str.strip()

    # Colunas que queremos manter
    colunas_desejadas = [
        "Carteira",
        "Pagador",
        "CPF/CNPJ Pagador",
        "Tipo",
        "Nosso Número",
        "Seu Número",
        "Data Emissão",
        "Data Vencimento",
        "Data Baixa",
        "Valor Título (R$)",
    ]

    df = df[colunas_desejadas]

    #converter datas

    df["Data Vencimento"] = pd.to_datetime(df["Data Vencimento"], dayfirst=true, errors="coerce")
    df["Data Baixa"] = pd.to_datetime(df["Data Baixa"], dayfirst=true, errors="coerce")

    #conversor de valores

    df["Valor Título (R$)"] = pd.to_numeric(df["Valor Título (R$)"], errors="coerce")

    return df

    #boletos vencidos
    def boletos_vencidos(df):
        hoje = pd.Timestamp.today().normalize()
        return df[(df["Data Vencimento"] < hoje) & (df["Data Baixa"].isna())]
    
    #boletos que vence em x dias
    def boletos_a_vencer(df, dias=5):
        hoje = pd.Timestamp.today().normalize()
        limite = hoje + pd.Timedelta(days=dia)

    #boletos sem baixa
    def total_em_aberto(df):