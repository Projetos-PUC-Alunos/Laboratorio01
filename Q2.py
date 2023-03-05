import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Jully K/Documents/projects/Laboratorio06/repositorios.csv', delimiter=';')

# Calcula a mediana da idade e da idade de atualização de todas as linhas
mediana_AcceptedPullRequests = df['AcceptedPullRequests'].median()

print(f"A mediana da total de pull requests é {mediana_AcceptedPullRequests}")

# cria o boxplot
plt.boxplot(df['AcceptedPullRequests'].dropna(), showfliers=False)

# adiciona rótulos e título
plt.xlabel('Total de Pull Requests')
plt.title('Boxplot do Total de Pull Requests')

# salva o gráfico como uma imagem
plt.savefig('boxplot_total_pullrequests_repositorios.png')

# exibe o gráfico
plt.show()