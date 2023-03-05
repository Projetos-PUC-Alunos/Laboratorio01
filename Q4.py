import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Jully K/Documents/projects/Laboratorio06/repositorios.csv', delimiter=';')

# Converte as colunas "updatedAt" para datetime
df['updatedAt'] = pd.to_datetime(df['updatedAt'], format='%Y-%m-%d')

# Remove as linhas com valores ausentes
df = df.dropna(subset=['updatedAt'])

# Calcula a idade de cada linha e adiciona a uma nova coluna "idade"
hoje = datetime.today().date()
df['updatedTime'] = (hoje - df['updatedAt'].dt.date).dt.days

# Calcula a mediana da idade e da idade de atualização de todas as linhas
mediana_updatedTime = df['updatedTime'].median()

print(f"A mediana do tempo de atualização é {mediana_updatedTime} dias")
# print(f"A mediana da idade de atualização é {mediana_idade_atualizacao} dias")

# cria o boxplot
plt.boxplot(df['updatedTime'],showfliers=False)

# adiciona rótulos e título
plt.xlabel('Tempo desde a última atualização')
plt.ylabel('Dias')
plt.title('Boxplot do Tempo desde a última atualização')

# salva o gráfico como uma imagem
plt.savefig('boxplot_tempo_atualização.png')

# exibe o gráfico
plt.show()