import streamlit as st
from datetime import date, timedelta
from contrato import Dados
from webscraping import obter_codigos #, buscar_dados
from teste import criar_dados
from genIA import ask_groq
from pydantic import ValidationError

def main():

    st.title('Informações Ações da Ibovespa')

    try:
        #acoes = obter_codigos()
        acoes = ['BRKM5', 'USIM5', 'CVCB3', 'RENT3']

        escolher_acao(acoes)

    except Exception as e:
        st.error(f"Ocorreu um erro durante ao obter a lista de ações: {str(e)}")
 

def escolher_acao(acoes):

    escolha = st.selectbox('Escolha qual ação deseja obter informações', acoes)
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

            buscar_informacoes(escolha, data_inicio, data_fim)

        except ValidationError as e:
            st.error(e)

def buscar_informacoes(escolha, data_inicio, data_fim):

    try:
        #df = buscar_dados(escolha, data_inicio, data_fim)
        df = criar_dados()

        st.success("Dados importados com sucesso!")
        st.dataframe(df)

        question = st.text_input(f"Qual a sua pergunta em relação a {escolha}")

        if st.button("Perguntar"):
            answer = ask_groq(question, df)
            st.write(answer)
    
    except Exception as e:
        st.error(f"Ocorreu um erro durante o web scraping: {str(e)}")


if __name__ == "__main__":
    main()