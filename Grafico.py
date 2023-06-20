# Importamos as bibliotecas necessárias para a aplicação.
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Leitura do arquivo CSV. Aqui, estamos removendo os números antes do ponto no início de cada linha usando uma função lambda.
df = pd.read_csv('Variacao.csv', delimiter=';', skiprows=1, skipfooter=1, decimal=',', encoding='utf8', converters={0: lambda x: x.split('.', 1)[-1]})

# Convertendo os valores no dataframe para um formato numérico.
df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Configurando a primeira coluna como o índice do dataframe.
df.set_index(df.columns[0], inplace=True)

# Transpondo o dataframe.
df_t = df.transpose()

# Criando uma caixa de seleção para o usuário escolher se quer visualizar todos os dados ou não.
plot_all_data = st.checkbox('Mostrar todos os dados')

# Definindo os tipos de gráficos que o usuário pode escolher.
chart_types = ['Linha', 'Barra', 'Dispersão']
chart_choice = st.selectbox("Selecione o tipo de gráfico:", options=chart_types)

# Definindo uma lista de cores.
colors = plt.cm.viridis(np.linspace(0, 1, len(df_t.columns)))

# Caso a caixa 'Mostrar todos os dados' seja selecionada, esta condição será executada.
if plot_all_data:
    fig, ax = plt.subplots(figsize=(15,10))
    for i, column in enumerate(df_t.columns):
        if chart_choice == 'Linha':
            sns.lineplot(x=df_t.index, y=df_t[column], label=column, ax=ax) 
        elif chart_choice == 'Barra':
            # Define uma cor diferente para cada gráfico de barras.
            sns.barplot(x=df_t.index, y=df_t[column], label=column, ax=ax, color=colors[i])
        elif chart_choice == 'Dispersão':
            sns.scatterplot(x=df_t.index, y=df_t[column], label=column, ax=ax)
            
    plt.title('Variações por cidade')
    plt.xlabel('Cidade')
    plt.ylabel('Valor')
    plt.xticks(rotation=90)
    plt.grid(True)

    # Aqui ajustamos os limites do eixo y para variar de acordo com os valores mínimos e máximos dos dados.
    min_val = df_t.min().min()  # Obtemos o valor mínimo de todos os dados.
    max_val = df_t.max().max()  # Obtemos o valor máximo de todos os dados.
    plt.ylim(min_val, max_val)  # Definimos os limites do eixo y.

    plt.legend()
    st.pyplot(fig)
else:
    # Criando uma caixa de seleção para o usuário escolher se quer filtrar por área.
    filter_by_area = st.checkbox('Filtrar por área')

    if filter_by_area:
        # Criando uma caixa de seleção com as áreas para o usuário escolher.
        area = st.selectbox("Selecione a área:", options=df_t.index.tolist())
        df_filtered = df_t.loc[area, :]

        # Plotando os dados filtrados.
        fig, ax = plt.subplots(figsize=(15,10))
        if chart_choice == 'Linha':
            sns.lineplot(x=df_filtered.index, y=df_filtered.values, label=area, ax=ax)
        elif chart_choice == 'Barra':
            sns.barplot(x=df_filtered.index, y=df_filtered.values, label=area, ax=ax)
        elif chart_choice == 'Dispersão':
            sns.scatterplot(x=df_filtered.index, y=df_filtered.values, label=area, ax=ax)
        plt.title('Variações por {}'.format(area))
        plt.xlabel('Grupos')
        plt.ylabel('Valor')
        plt.xticks(rotation=90)
        plt.grid(True)
        min_val = df_filtered.min()  # Obtemos o valor mínimo dos dados filtrados.
        max_val = df_filtered.max()  # Obtemos o valor máximo dos dados filtrados.
        plt.ylim(min_val, max_val)  # Definimos os limites do eixo y.
        plt.legend()
        st.pyplot(fig)
    else:
        # Criando uma caixa de seleção com os grupos para o usuário escolher.
        group = st.selectbox("Selecione o grupo:", options=df_t.columns.tolist())
        df_filtered = df_t[group]

        # Plotando os dados filtrados.
        fig, ax = plt.subplots(figsize=(15,10))
        if chart_choice == 'Linha':
            sns.lineplot(x=df_filtered.index, y=df_filtered.values, label=group, ax=ax)
        elif chart_choice == 'Barra':
            sns.barplot(x=df_filtered.index, y=df_filtered.values, label=group, ax=ax)
        elif chart_choice == 'Dispersão':
            sns.scatterplot(x=df_filtered.index, y=df_filtered.values, label=group, ax=ax)
        plt.title('Variações para {}'.format(group))
        plt.xlabel('Área')
        plt.ylabel('Valor')
        plt.xticks(rotation=90)
        plt.grid(True)
        min_val = df_filtered.min()  # Obtemos o valor mínimo dos dados filtrados.
        max_val = df_filtered.max()  # Obtemos o valor máximo dos dados filtrados.
        plt.ylim(min_val, max_val)  # Definimos os limites do eixo y.
        plt.legend()
        st.pyplot(fig)
