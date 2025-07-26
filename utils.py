import streamlit as st

def show_header(show_calculadora=True):

    # Barra superior
    st.image("imagem/novo_ciclo_sup1.png", use_container_width=True)
    
    # Links com imagens e botões reais
    col1, col2, col3, col4 = st.columns([3, 1, 1,1 ])
    if show_calculadora:

        with col2:
            st.page_link("pages/Dashboard.py", label= "**Análise Resíduos BH**")
    
        with col4:
            st.page_link("https://novocicloresiduos.com.br/", label="**Sobre o Projeto**")
    
        # Imagem indicadora da calculadora
        st.image("imagem/calculadora_circulos.png", use_container_width=True)

    else:
        with col2:
            st.page_link("app.py", label="**Calculadora de impacto coleta seletiva**")
    
        with col4:
             st.page_link("https://novocicloresiduos.com.br/", label="**Sobre o Projeto**")
        

def show_footer():
    st.markdown("---")
    st.image("imagem/logos.png", use_container_width=True)