import streamlit as st
from datetime import date, timedelta
from contrato import Dados

def main():
    st.title('Informações Ações da Ibovespa')

    acoes = ['AZUL4', 'CVCB3', 'JBSS3', 'PETZ3']

    escolha = st.selectbox('Escolha qual ação deseja obter informações', acoes)
    data_inicio = st.date_input('Escolha a data inicial', date.today())
    data_fim = st.date_input('Escolha a data final', date.today() - timedelta(days=30))

    if st.button("Analisar"):

        validacao = Dados(
            escolha = escolha, 
            data_inicio = data_inicio, 
            data_fim = data_fim
        )

        st.write(escolha)
        st.write(data_inicio)
        st.write(data_fim)

if __name__ == "__main__":
    main()