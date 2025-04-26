import pandas as pd

# Criar um DataFrame com os dados
dados = {
    "Nome": ["Ana", "Bruno", "Carlos"],
    "Idade": [23, 35, 29],
    "Cidade": ["Lisboa", "Porto", "Coimbra"]
}

tabela = pd.DataFrame(dados)

# Salvar o DataFrame como um arquivo Excel
tabela.to_excel("DB_Excel.xlsx", index=False)

print("Arquivo 'DB_Excel.xlsx' criado com sucesso!")
