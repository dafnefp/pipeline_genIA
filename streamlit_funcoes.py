import streamlit as st
from datetime import date, timedelta
from contrato import Dados
# from webscraping import obter_codigos, buscar_dados
from teste import criar_dados
from genIA import ask_groq
from pydantic import ValidationError


def busca_acoes():
    if "scraping_inicializado" not in st.session_state:
        st.session_state.scraping_inicializado = True

    try:
        #st.session_state.acoes = obter_codigos()
        st.session_state.acoes = ['BRKM5', 'USIM5', 'CVCB3', 'RENT3']

    except Exception as e:
        st.error(f"Ocorreu um erro durante ao obter a lista de ações: {str(e)}")


def escolher_acao():
    if "escolha" not in st.session_state:
        escolha = st.selectbox('Escolha qual ação deseja obter informações', st.session_state.acoes)
        data_inicio = st.date_input('Escolha a data inicial', date.today() - timedelta(days=30))
        data_fim = st.date_input('Escolha a data final', date.today())

        if st.button("Analisar"):
            try: 
                validacao = Dados(
                    escolha = escolha, 
                    data_inicio = data_inicio, 
                    data_fim = data_fim
                )
                st.write(validacao)

                st.session_state.dados_usuario_enviado = True

                st.session_state.escolha = escolha
                st.session_state.data_inicio = data_inicio
                st.session_state.data_fim = data_fim

            except ValidationError as e:
                st.error(e)

def buscar_informacoes():
    if "dados_usuario_enviado" in st.session_state:
        try:
            #df = buscar_dados(st.session_state.escolha, st.session_state.data_inicio, st.session_state.data_fim)
            df = criar_dados()
            st.success("Dados importados com sucesso!")            
            st.session_state.df = df
        
        except Exception as e:
            st.error(f"Ocorreu um erro durante o web scraping: {str(e)}")


def perguntas():
    if "dados_usuario_enviado" in st.session_state:
        question = st.text_input(f"Qual a sua pergunta em relação a {st.session_state.escolha}")

        if st.button("Perguntar"):
            try:
                answer = ask_groq(question, st.session_state.df)
                st.write(answer)

            except Exception as e:
                st.error(f"Ocorreu um erro: {str(e)}")