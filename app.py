import streamlit as st
from streamlit_funcoes import busca_acoes, escolher_acao, buscar_informacoes, perguntas

def main():
    st.title('Informações Ações da Ibovespa')

    # Passo 1: Inicializa o web scraping para buscar a lista de ações disponíveis
    busca_acoes()

    # Passo 2: Usuário escolhe a ação e seleciona o período das informações
    escolher_acao()

    # Passo 3: Inicializa o web scraping para buscar as informações dos dados selecionados pelo usuário
    buscar_informacoes()

    # Passo 4: Pergunta a IA sobre os dados
    perguntas()
       

if __name__ == "__main__":
    main()