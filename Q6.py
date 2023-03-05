import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Jully K/Documents/projects/Laboratorio06/repositorios.csv', delimiter=';')

# filtra as linhas onde totalIssues é diferente de zero, elas serão desconsideradas
df = df[df['totalIssues'] != 0]

# calcular a razão entre as colunas closedIssues e totalIssues
df['ratio'] = df['closedIssues'] / df['totalIssues'] * 100

# calcular a mediana dos valores de ratio
median_ratio = np.median(df['ratio'])

# imprimir a mediana
print(f"A mediana do Total de Issues fechadas é {median_ratio}")

# criar um boxplot da nova coluna
plt.boxplot(df['ratio'],showfliers=False)

# adiciona rótulos e título
plt.ylabel('Percentual de Total de Issues fechadas')
plt.title('Boxplot do percentual de total de Issues fechadas')

# # salva o gráfico como uma imagem
plt.savefig('boxplot_clossed_issues_percent_repositorios.png')

# exibir o gráfico
plt.show()
