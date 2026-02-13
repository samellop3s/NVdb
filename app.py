from processamento import carregar_planilha 

arquivo = "uploads/BL pagos NV.xlsx"


df = carregar_planilha(arquivo)

print(df.head())