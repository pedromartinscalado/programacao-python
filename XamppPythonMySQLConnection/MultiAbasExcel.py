import pandas as pd

# Criar dois DataFrames
dados1 = pd.DataFrame({
    "Nome": ["Ana", "Bruno", "Carlos"],
    "Idade": [23, 35, 29]
})

dados2 = pd.DataFrame({
    "Produto": ["Caneta", "Caderno", "Lápis"],
    "Preço": [1.5, 2.0, 0.5]
})

# Salvar os DataFrames em abas separadas
with pd.ExcelWriter("multi_abas.xlsx") as writer:
    dados1.to_excel(writer, sheet_name="Pessoas", index=False)
    dados2.to_excel(writer, sheet_name="Produtos", index=False)

# Confirmar que o arquivo foi criado com sucesso
print("Arquivo 'multi_abas.xlsx' criado com sucesso com múltiplas abas.")
