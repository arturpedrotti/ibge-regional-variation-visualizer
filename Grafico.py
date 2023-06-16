import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lendo a função para ler o CSV, pulamos a primeira e última linha do arquivo. Estamos abrindo e lendo a pasta
# Usamos a função lambda para remover os números antes do ponto no início de cada linha.
df = pd.read_csv('Variacao.csv', delimiter=';', skiprows=1, skipfooter=1, decimal=',', encoding='utf8', converters={0: lambda x: x.split('.', 1)[-1]})

# Convertendo os valores no dataframe para um formato numerico
df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Configurando a primeira coluna como o indice
df.set_index(df.columns[0], inplace=True)

# Transpondo o dataframe para inverter as linhas e colunas do dataframe.
df_t = df.transpose()

# checkbox caso o usuário queira que todos os dados no gráfico sejam demonstrados.
plot_all_data = st.checkbox('Mostrar todos os dados')

if plot_all_data:
    fig, ax = plt.subplots(figsize=(15,10))
    for column in df_t.columns:
        sns.lineplot(x=df_t.index, y=df_t[column], label=column, ax=ax) 
    plt.title('Variações por cidade')
    plt.xlabel('Cidade')
    plt.ylabel('Valor')
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.ylim(-2, 2)
    plt.legend()
    st.pyplot(fig)
else:
    filter_by_area = st.checkbox('Filtrar por area')

    if filter_by_area:
        area = st.selectbox("Selecione a area:", options=df_t.index.tolist())
        df_filtered = df_t.loc[area, :]
        
        fig, ax = plt.subplots(figsize=(15,10))
        sns.lineplot(x=df_filtered.index, y=df_filtered.values, label=area, ax=ax)
        plt.title('Variações por {}'.format(area))
        plt.xlabel('Grupos')
        plt.ylabel('Valor')
        plt.xticks(rotation=90)
        plt.grid(True)
        plt.ylim(-2, 2)
        plt.legend()
        st.pyplot(fig)
    else:
        group = st.selectbox("Selecione o grupo:", options=df_t.columns.tolist())
        df_filtered = df_t[group]
        fig, ax = plt.subplots(figsize=(15,10))
        sns.lineplot(x=df_filtered.index, y=df_filtered.values, label=group, ax=ax)
        plt.title('Variações para {}'.format(group))
        plt.xlabel('Area')
        plt.ylabel('Valor')
        plt.xticks(rotation=90)
        plt.grid(True)
        plt.ylim(-2, 2)
        plt.legend()
        st.pyplot(fig)
