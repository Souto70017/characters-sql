import streamlit as st
import page.insert as insert
import page.select as select
import page.update as update
import page.delete as delete


st.sidebar.title('Personagens')
page = st.sidebar.selectbox('menu',['Inserir','Consultar','Alterar','Deletar'])

if page == 'Consultar':
    select.consultar()
if page == 'Inserir':
    insert.inserir()
if page == 'Alterar':
    update.alterar()
if page == 'Deletar':
    delete.deletar()