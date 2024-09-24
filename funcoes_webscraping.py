import streamlit as st
# from webscraping import obter_codigos, buscar_dados
from teste import criar_dados
from time import sleep


def busca_acoes():
    if "scraping_inicializado" not in st.session_state:
        with st.spinner("Coletando lista de ações, aguarde..."):
            try:
                #st.session_state.acoes = obter_codigos()
                sleep(5)
                st.session_state.acoes = ['BRKM5', 'USIM5', 'CVCB3', 'RENT3']
                st.session_state.scraping_inicializado = True

            except Exception as e:
                st.error(f"Ocorreu um erro ao obter a lista de ações: {str(e)}")


def buscar_informacoes(escolha, data_inicio, data_fim):
    if "webscraping_infos" not in st.session_state and escolha:
        try:
            placeholder = st.empty() 
            
            with placeholder.container():
                st.info("Coletando informações baseadas nos dados fornecidos...")
                # df = buscar_dados(st.session_state.escolha, st.session_state.data_inicio, st.session_state.data_fim)
                sleep(5)
                df = criar_dados()
                st.session_state['webscraping_infos'] = True
            
            placeholder.empty()
            st.success("Dados coletados com sucesso!")            
            st.session_state.df = df
        
        except Exception as e:
            st.error(f"Ocorreu um erro durante o web scraping: {str(e)}")