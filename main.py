# Importando as Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# Carregar o dataset (arquivo CSV)
df = pd.read_csv('world.csv')

# Paises para comparação: Brasil e Venezuela
country_1 = 'Brazil'
country_2 = 'Venezuela'

# Filtrar os dados do Brasil
df_1 = df[df['Country'] == country_1]

# Filtrar os dados dos Estados Unidos
df_2 = df[df['Country'] == country_2]

# Ajustar os valores em porcentagem
df_1['happiness_score_pct'] = df_1['happiness_score'] * 10
df_2['happiness_score_pct'] = df_2['happiness_score'] * 10

# Plotar o gráfico de linhas para o Brasil
plt.plot(df_1['Year'], df_1['happiness_score_pct'], marker='o', label=country_1)

# Plotar o gráfico de linhas para os Estados Unidos
plt.plot(df_2['Year'], df_2['happiness_score_pct'], marker='o', label=country_2)

plt.xlabel('Ano')
plt.ylabel('Pontuação de Felicidade (%)')
plt.title(f'Pontuação de Felicidade  {country_1} x {country_2} ao longo dos anos')
plt.grid(True)

# Definir o intervalo do eixo y
plt.ylim(0, 100)

# Adicionar a legenda
plt.legend()
# Mostra o gráfico
plt.show()


# Grafico de barras

# Ordena os dados pela coluna "happiness_rate" em ordem decrescente
sorted_data = df.sort_values(by='happiness_score', ascending=False)

# Seleciona os 20 países com maior pontuação de felicidade
top_coutries_bar = sorted_data.drop_duplicates(subset='Country').head(20)

# Cria o gráfico de barras
plt.bar(top_coutries_bar['Country'], top_coutries_bar['happiness_score'])
plt.xlabel('País')
plt.ylabel('Pontuação de Felicidade')
plt.title('Top 20 Países com Maior Pontuação de Felicidade')
plt.xticks(rotation=90)
plt.grid(True, axis='y')

# Exibe o gráfico
plt.show()


# Grafico do tipo Treemap

# Cria o dataframe com os dados da América do Sul em 2020
treemap_df = df[(df['continent'] == 'South America') & (df['Year'] == 2020)]

# Ordena os países pela pontuação de felicidade em ordem decrescente
treemap_df = treemap_df.sort_values('happiness_score', ascending=False)

# Selecionar os 5 primeiros e os 5 últimos países
top_countries = treemap_df.head(10)
bottom_countries = treemap_df.tail(10)

# Concatenar os dois dataframes em uma única tabela
combined_df = pd.concat([top_countries, bottom_countries])

# Criar o gráfico treemap
fig = px.treemap(combined_df, path=['Country'], values='happiness_score')
# Adicionar título ao gráfico
fig.update_layout(title_text='Top 10 e Últimos 10 Pontuação de Felicidade na América do Sul em 2020')
fig.update_traces(textinfo='label+percent entry')

# Exibir o gráfico
fig.show()