import pandas as pd

# Definir o nome do arquivo Excel
arquivo = "DB_Excel.xlsx"

# Ler o arquivo Excel
tabela = pd.read_excel(arquivo)

# Alterar valores no DataFrame
tabela.loc[tabela["Nome"] == "Ana", "Idade"] = 24  # Atualiza a idade da Ana
tabela.loc[tabela["Nome"] == "Carlos", "Cidade"] = "Guimarães"  # Atualiza a cidade de Carlos

# Salvar as alterações no mesmo arquivo
tabela.to_excel(arquivo, index=False)

# Confirmar que os dados foram atualizados
print(f"Dados atualizados no arquivo '{arquivo}'.")
