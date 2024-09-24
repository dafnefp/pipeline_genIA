import sys, os.path
application_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/modules/')
sys.path.append(application_dir)

import streamlit as st
import dados.funcoes_dados as fd
import webscraping.funcoes_webscraping as fw


def main():
    st.title('Informações Ações da Ibovespa')

    # Passo 1: Inicializa o web scraping para buscar a lista de ações disponíveis
    fw.busca_acoes()

    # Passo 2: Usuário escolhe a ação e seleciona o período das informações
    escolha, data_inicio, data_fim = fd.escolher_acao()

    if st.button("Analisar"):
        fd.validar_dados(escolha, data_inicio, data_fim)
        
        # Passo 3: Inicializa o web scraping para buscar as informações dos dados selecionados pelo usuário
        fw.buscar_informacoes(escolha, data_inicio, data_fim)

    # Passo 4: Pergunta a IA sobre os dados
    fd.perguntas(escolha)

    if 'ia_resposta' in st.session_state:
        if st.button("Resetar aplicação"):
                st.session_state.clear()
                st.rerun()  # Recarrega a página para reiniciar
       

if __name__ == "__main__":
    main()