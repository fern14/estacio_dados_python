import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv('dados_microempreendedores.csv')

# Análise básica
print(df.describe())

# Visualização da distribuição de renda
plt.figure(figsize=(10, 6))
sns.histplot(df['renda_mensal'], kde=True)
plt.title('Distribuição de Renda dos Microempreendedores')
plt.xlabel('Renda Mensal (R$)')
plt.ylabel('Frequência')
plt.savefig('distribuicao_renda.png')
plt.close()

# Análise de correlação entre idade e renda
correlation = df['idade'].corr(df['renda_mensal'])
print(f"Correlação entre idade e renda: {correlation}")

# Agrupamento por setor de atuação
setor_stats = df.groupby('setor')['renda_mensal'].agg(['mean', 'median', 'count'])
print(setor_stats)

# Exportar resultados
setor_stats.to_csv('estatisticas_por_setor.csv')

# Identificar oportunidades de negócio
oportunidades = df[df['renda_mensal'] > df['renda_mensal'].mean()]
print(f"Número de microempreendedores com renda acima da média: {len(oportunidades)}")

# Criar um dashboard simples (exemplo básico)
import streamlit as st

st.title('Dashboard de Microempreendedores')

st.write("Estatísticas por Setor:")
st.dataframe(setor_stats)

st.write("Distribuição de Renda:")
st.image('distribuicao_renda.png')

st.write(f"Correlação entre idade e renda: {correlation:.2f}")

st.write(f"Microempreendedores com renda acima da média: {len(oportunidades)}")