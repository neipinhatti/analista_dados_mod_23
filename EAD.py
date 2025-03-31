# Análise Exploratória de Dados (EAD)
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
print(df)

# Verificando correlações
df_corr = df[['N_Avaliações', 'Qtd_Vendidos_Cod', 'Desconto', 'Nota', 'Preço', 'Material_Cod', 'Temporada_Cod',
              'Marca_Cod']].corr()
print(df_corr.to_string())

print(df.info())

print('\nAnálise da dados nulos:\n', df.isnull().sum())
print('% de dados nulos:\n', df.isnull().mean() * 100)
# df.dropna(inplace=True)
# print('\nConfirmar remoção de dados nulos\n', df.isnull().sum().sum())

print('Análise de dados duplicados: \n', df.duplicated().sum())
# df.drop_duplicates()
# print('Duplicados após drop: \n', df.duplicated().sum())

print("Análise de dados únicos: \n", df.nunique())

print('Estatísticas dos dados:\n', df.describe())

df.to_csv('ecommerce_tratado.csv')
