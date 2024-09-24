import sys, os.path
application_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/modules/')
sys.path.append(application_dir)

import streamlit as st
from datetime import date, timedelta
from pydantic import ValidationError
import dados.contrato as ct
import inteligencia_artificial.genIA as ia


def escolher_acao():
    if "dados_usuario_enviado" not in st.session_state:
        escolha = st.selectbox('Escolha qual ação deseja obter informações', st.session_state.acoes)
        data_inicio = st.date_input('Escolha a data inicial', date.today() - timedelta(days=30))
        data_fim = st.date_input('Escolha a data final', date.today())
    
    return escolha, data_inicio, data_fim


def validar_dados(escolha, data_inicio, data_fim):
    try: 
        validacao = ct.Dados(
            escolha = escolha, 
            data_inicio = data_inicio, 
            data_fim = data_fim
        )
    except ValidationError as e:
        st.error(e)


def perguntas(escolha):
    if 'ia_resposta' not in st.session_state and "webscraping_infos" in st.session_state:
        question = st.text_input(f"Qual a sua pergunta em relação a {escolha}")

        if st.button("Perguntar"):
            try:
                with st.spinner("Consultando a IA, aguarde..."):
                    answer = ia.ask_groq(question, st.session_state.df)
                    st.session_state['ia_resposta'] = True
                    st.write(answer)

            except Exception as e:
                st.error(f"Ocorreu um erro: {str(e)}")