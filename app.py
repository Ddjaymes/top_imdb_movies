import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
movies_imdb = pd.read_csv('IMDB Top 250 Movies.csv')

st.header('Melhores filmes de acordo com o IMDB')
st.subheader('Conjunto de dados dos melhores filmes de acordo com o IMDB')

movies_data = pd.read_csv('IMDB Top 250 Movies.csv') # lendo os dados
hist_button = st.button('Criando histograma') # criar um botão
       
if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados dos melhores filmes...')
            
    # criar um histograma
    fig = px.histogram(movies_data, x = "rating")
            
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão') # criar um botão

if scatter_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados dos melhores filmes...')
            
    # criar um histograma
    fig = px.scatter(movies_data, x = "rating", y = 'genre')
            
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width = True)
