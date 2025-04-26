import pandas as pd
import os

# Definir o nome do arquivo Excel
arquivo = "DB_Excel.xlsx"

# Verificar se o arquivo já existe
if os.path.exists(arquivo):
    # Ler a folha de Excel existente
    tabela = pd.read_excel(arquivo)
else:
    # Se o arquivo não existir, criar um DataFrame vazio
    tabela = pd.DataFrame(columns=["Nome", "Idade", "Cidade"])

# Adicionar novos dados ao DataFrame
novos_dados = pd.DataFrame({
    "Nome": ["Diana", "Eduardo"],
    "Idade": [30, 28],
    "Cidade": ["Aveiro", "Faro"]
})

# Concatenar os dados existentes com os novos dados
tabela_atualizada = pd.concat([tabela, novos_dados], ignore_index=True)

# Remover duplicatas com base na coluna "Nome"
tabela_atualizada = tabela_atualizada.drop_duplicates(subset="Nome", keep="last")

# Salvar a folha atualizada de volta no arquivo
tabela_atualizada.to_excel(arquivo, index=False)

# Confirmar que os dados foram adicionados
print(f"Novos dados adicionados ao arquivo '{arquivo}'.")
