import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Jully K/Documents/projects/Laboratorio06/repositorios.csv', delimiter=';')

# Converte as colunas "createdAt" e "updatedAt" para datetime
df['createdAt'] = pd.to_datetime(df['createdAt'], format='%Y-%m-%d')
df['updatedAt'] = pd.to_datetime(df['updatedAt'], format='%Y-%m-%d')

# Remove as linhas com valores ausentes
df = df.dropna(subset=['createdAt', 'updatedAt'])

# Calcula a idade de cada linha e adiciona a uma nova coluna "idade"
hoje = datetime.today().date()
df['idade'] = (hoje - df['createdAt'].dt.date).dt.days

# Calcula a mediana da idade e da idade de atualização de todas as linhas
mediana_idade = df['idade'].median()

print(f"A mediana da idade é {mediana_idade} dias")
# print(f"A mediana da idade de atualização é {mediana_idade_atualizacao} dias")

# cria o boxplot
plt.boxplot(df['idade'])

# adiciona rótulos e título
plt.xlabel('Idade')
plt.ylabel('Dias')
plt.title('Boxplot da idade dos repositórios')

# salva o gráfico como uma imagem
plt.savefig('boxplot_idade_repositorios.png')

# exibe o gráfico
plt.show()