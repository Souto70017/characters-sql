import streamlit as st
import controller.cliente as cliente


def inserir():
    st.title('Inserir Dados')
    
    with st.form(key='insert'):
        input_name = st.text_input(label='Insira o nome')
        input_discricao = st.text_input(label='Insira a Descrição')
        input_link = st.text_input(label='Insira um link')
        input_programa = st.text_input(label='Insira o programa')
        input_animador = st.text_input(label='Insira o animador')
        button_submit = st.form_submit_button('Enviar')

        if button_submit:
            cliente.incluir(input_name, input_discricao, input_link, input_programa, input_animador)
            st.success('Cliente incluido com sucesso!!!')