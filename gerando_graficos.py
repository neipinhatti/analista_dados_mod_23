import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('ecommerce_tratado.csv')

print(df.head(30).to_string())

# Verificando correlações
df_corr = df[['N_Avaliações', 'Qtd_Vendidos_Cod', 'Desconto', 'Nota', 'Preço', 'Material_Cod', 'Temporada_Cod',
              'Marca_Cod']].corr()

# Histograma - Parâmetros
plt.figure(figsize=(10, 6))
plt.hist(df['Nota'], bins=30, color='Blue', alpha=0.8)
plt.title('Histograma - Produto e Nota')
plt.xlabel('Nota')
plt.ylabel('Frequência')
plt.grid(False)
plt.show()

# Gráficos de Dispersão
plt.hexbin(df['Preço'], df['N_Avaliações'], gridsize=25, cmap='Greens')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Preço')
plt.ylabel('Número de Avaliações')
plt.title('Dispersão de Preço e Número de Avaliações')
plt.show()

# Mapa de Calor
plt.figure(figsize=(10, 6))
sns.heatmap(df_corr, annot=True, fmt=".2f")
plt.title('Mapa de Calor de Correlação entre Variáveis')
plt.show()

# Gráficos de barras
top_n = 10
contagem_marcas = df['Marca'].value_counts()
top_marcas = contagem_marcas.head(top_n)
# outras = pd.Series({'Outras': contagem_marcas.iloc[top_n:].sum()})
# contagem_agrupada = pd.concat([top_marcas])
plt.figure(figsize=(10, 6))
top_marcas.plot(kind='bar', color='#90ee70')
plt.title(f'Top {top_n} Marcas')
plt.xlabel('Marca')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico de pizza
x = df['Gênero'].value_counts().index
y = df['Gênero'].value_counts().values
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição de Vendas por Gênero')
plt.show()

# Gráfico de densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'], fill=True, color='#863e9c')
plt.title('Densidade de Preço')
plt.xlabel('Preço')
plt.show()

# Gráfico de Regressão
sns.regplot(x='Desconto', y='Qtd_Vendidos_Cod', data=df, color='#278f65',
            scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de Desconto por Quantidade Vendida')
plt.xlabel('Desconto')
plt.ylabel('Quantidade')
plt.show()
