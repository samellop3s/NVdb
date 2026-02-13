import pandas as pd


def carregar_planilha(caminho_arquivo):
    df = pd.read_excel(caminho_arquivo, skiprows=6)

    df.columns = df.columns.str.strip()

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

    df["Data Vencimento"] = pd.to_datetime(
        df["Data Vencimento"], dayfirst=True, errors="coerce"
    )

    df["Data Baixa"] = pd.to_datetime(
        df["Data Baixa"], dayfirst=True, errors="coerce"
    )

    df["Valor Título (R$)"] = pd.to_numeric(
        df["Valor Título (R$)"], errors="coerce"
    )

    return df


# 📅 Boletos vencidos
def boletos_vencidos(df):
    hoje = pd.Timestamp.today().normalize()
    return df[(df["Data Vencimento"] < hoje) & (df["Data Baixa"].isna())]


# ⏳ Boletos a vencer em X dias
def boletos_a_vencer(df, dias=5):
    hoje = pd.Timestamp.today().normalize()
    limite = hoje + pd.Timedelta(days=dias)

    return df[
        (df["Data Vencimento"] >= hoje)
        & (df["Data Vencimento"] <= limite)
        & (df["Data Baixa"].isna())
    ]


# 🚨 Boletos sem baixa
def boletos_sem_baixa(df):
    return df[df["Data Baixa"].isna()]


# 💰 Total em aberto
def total_em_aberto(df):
    em_aberto = df[df["Data Baixa"].isna()]
    return em_aberto["Valor Título (R$)"].sum()


# 📊 Resumo financeiro
def resumo_financeiro(df):
    total_geral = df["Valor Título (R$)"].sum()
    total_aberto = total_em_aberto(df)
    total_pago = total_geral - total_aberto

    return {
        "Total Geral": total_geral,
        "Total em Aberto": total_aberto,
        "Total Pago": total_pago,
    }
