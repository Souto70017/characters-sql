import streamlit as st
import controller.cliente as cliente


def alterar():
    if "upda" not in st.session_state:
        st.session_state.upda = False

    st.title('Alterar Dados')
  

    update_id = st.number_input(label='Insira o Id', format='%d', step=1)
    button_update_select = st.button('Consultar')

    if button_update_select:
        st.session_state.upda = True

    if st.session_state.upda == True:
        item = cliente.selecionar_id(update_id)[0]
        with st.form(key='update'):
            update_name = st.text_input(label='Insira o nome', value=item[1])
            update_discricao = st.text_input(label='Insira a Discrição', value=item[2])
            update_link = st.text_input(label='Insira o link', value=item[3])
            update_programa = st.text_input(label='Insira o programa', value=[4])
            update_animador = st.text_input(label='Insira o animador', value=[4])
            button_update = st.form_submit_button('Alterar')

            if button_update:
                cliente.alterar(update_name, update_discricao, update_link, update_programa, update_animador, item[0])
                st.success('Cliente alterado com sucesso!!!')
                st.session_state.upda = False