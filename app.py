from processamento import (
    carregar_planilha,
    boletos_vencidos,
    boletos_a_vencer,
    boletos_sem_baixa,
    total_em_aberto,
    resumo_financeiro
)

arquivo = "uploads/BL pagos NV.xlsx"

df = carregar_planilha(arquivo)

print("📅 VENCIDOS:")
print(boletos_vencidos(df))

print("\n⏳ A VENCER (5 dias):")
print(boletos_a_vencer(df, 5))

print("\n🚨 SEM BAIXA:")
print(boletos_sem_baixa(df))

print("\n💰 TOTAL EM ABERTO:")
print(total_em_aberto(df))

print("\n📊 RESUMO FINANCEIRO:")
print(resumo_financeiro(df))
