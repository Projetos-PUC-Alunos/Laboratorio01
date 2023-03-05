import pandas as pd
import matplotlib.pyplot as plt

# lê o arquivo CSV para um DataFrame
df = pd.read_csv('C:/Users/Jully K/Documents/projects/Laboratorio06/repositorios.csv', delimiter=';')

# conta a frequência de cada linguagem primária
freq_linguagens = df['PrimaryLanguage'].value_counts()

# cria o histograma
freq_linguagens.plot(kind='bar')
plt.xlabel('Linguagem Primária')
plt.ylabel('Frequência')
plt.title('Histograma de Frequência de Linguagens Primárias')

# salva o gráfico como uma imagem
plt.savefig('histogram_linguagens_populares.png')

# mostra o histograma
plt.show()
