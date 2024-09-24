import streamlit as st
from funcoes_webscraping import busca_acoes, buscar_informacoes
from funcoes_dados import escolher_acao, validar_dados, perguntas

def main():
    st.title('Informações Ações da Ibovespa')

    # Passo 1: Inicializa o web scraping para buscar a lista de ações disponíveis
    busca_acoes()

    # Passo 2: Usuário escolhe a ação e seleciona o período das informações
    escolha, data_inicio, data_fim = escolher_acao()

    if st.button("Analisar"):
        validar_dados(escolha, data_inicio, data_fim)
        
        # Passo 3: Inicializa o web scraping para buscar as informações dos dados selecionados pelo usuário
        buscar_informacoes(escolha, data_inicio, data_fim)

    # Passo 4: Pergunta a IA sobre os dados
    perguntas(escolha)

    if 'ia_resposta' in st.session_state:
        if st.button("Resetar aplicação"):
                st.session_state.clear()
                st.rerun()  # Recarrega a página para reiniciar
       

if __name__ == "__main__":
    main()