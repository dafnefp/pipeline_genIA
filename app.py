import streamlit as st
from datetime import date, timedelta
from contrato import Dados
from webscraping import obter_codigos
from pydantic import ValidationError

def main():
    st.title('Informações Ações da Ibovespa')

    #acoes = obter_codigos()
    acoes = ['BRKM5', 'USIM5', 'CVCB3', 'RENT3']

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

        except ValidationError as e:
            st.error(e)

 

if __name__ == "__main__":
    main()