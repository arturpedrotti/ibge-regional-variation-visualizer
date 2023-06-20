
import streamlit as st # streamlit é a biblioteca que nos permite criar aplicações web com Python.
import pandas as pd #biblioteca de manipulação de dados que usaremos para ler e tratar nossos dados.
# Seaborn e matplotlib são bibliotecas de visualização que nos permitirão criar gráficos a partir dos nossos dados.
import seaborn as sns
import matplotlib.pyplot as plt

# Usamos a função read_csv do pandas para ler o arquivo CSV onde nossos dados estão armazenados. 
# Estamos lendo o arquivo 'Variacao.csv', que tem seus valores separados por ponto e vírgula (';'), indicado pelo parâmetro delimiter.
# Os parâmetros skiprows e skipfooter nos permitem ignorar a primeira e a última linha do arquivo
# Estamos tratando números decimais que usam vírgulas como separador decimal, conforme indicado pelo parâmetro 'decimal'.
# O parâmetro 'converters' é usado para aplicar uma função aos valores antes deles serem lidos. Aqui, estamos usando uma função lambda (conhecido como função anonima) para remover quaisquer dígitos antes do ponto na primeira coluna.
df = pd.read_csv('Variacao.csv', delimiter=';', skiprows=1, skipfooter=1, decimal=',', encoding='utf8', converters={0: lambda x: x.split('.', 1)[-1]})

# Aqui, estamos convertendo os valores em todas as colunas (exceto a primeira) para valores numéricos.
# 'errors=coerce' faz com que qualquer valor que não possa ser convertido em um número seja substituído por NaN.
df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Neste passo, definimos a primeira coluna do nosso DataFrame como o índice. Isso é útil porque esses valores são únicos e podem ser usados para identificar as linhas.
df.set_index(df.columns[0], inplace=True)

# A função transpose é usada aqui para transformar as linhas em colunas e vice-versa. Isso é útil para facilitar a visualização e manipulação de nossos dados.
df_t = df.transpose()

# Usamos Streamlit para criar uma caixa de seleção que permite ao usuário escolher se deseja mostrar todos os dados ou não.
plot_all_data = st.checkbox('Mostrar todos os dados')

# Se a caixa 'Mostrar todos os dados' estiver marcada, todos os dados são plotados em um gráfico.
if plot_all_data:
    # Criamos uma figura e um conjunto de eixos para o nosso gráfico. 
    fig, ax = plt.subplots(figsize=(15,10))
    for column in df_t.columns:
        # Para cada coluna no nosso DataFrame transposto, criamos um gráfico de linha dos dados daquela coluna. 
        sns.lineplot(x=df_t.index, y=df_t[column], label=column, ax=ax) 
    # Adicionamos títulos e rótulos para o gráfico e os eixos, para facilitar a compreensão.
    plt.title('Variações por cidade')
    plt.xlabel('Cidade')
    plt.ylabel('Valor')
    # Rotacionamos os rótulos do eixo x em 90 graus para que não se sobreponham.
    plt.xticks(rotation=90)
    # Ativamos as linhas de grade no gráfico para facilitar a leitura dos valores.
    plt.grid(True)
    # Limitamos o eixo y para que ele vá de -2 a 2, pois sabemos que nossos dados caem nesse intervalo.
    plt.ylim(-2, 2)
    # Ativamos a legenda para que saibamos a que cidade cada linha corresponde.
    plt.legend()
    # Finalmente, usamos Streamlit para mostrar o gráfico na nossa aplicação web.
    st.pyplot(fig)
else:
    # Se a caixa 'Mostrar todos os dados' não estiver marcada, damos ao usuário a opção de filtrar os dados por área.
    filter_by_area = st.checkbox('Filtrar por area')

    if filter_by_area:
        # Se o usuário optar por filtrar por área, damos a ele uma caixa de seleção onde ele pode escolher a área desejada.
        area = st.selectbox("Selecione a area:", options=df_t.index.tolist())
        # Filtramos os dados para incluir apenas os da área selecionada.
        df_filtered = df_t.loc[area, :]
        
        #  plotando apenas os dados da área selecionada.
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
        # Se o usuário não optar por filtrar por área, damos a ele a opção de escolher um grupo específico para visualizar.
        group = st.selectbox("Selecione o grupo:", options=df_t.columns.tolist())
        # Filtramos os dados para incluir apenas os do grupo selecionado.
        df_filtered = df_t[group]
        # Novamente, o código aqui é muito semelhante ao código para o gráfico de todos os dados, mas estamos plotando apenas os dados do grupo selecionado.
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
