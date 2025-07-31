import streamlit as st
<<<<<<< HEAD
from utils import show_header, show_footer, is_mobile


#  Configuração de layout
st.set_page_config(
    layout="wide", 
    page_title="Dashboard de Resíduos",
    initial_sidebar_state="collapsed"
)


    
#  Detecta se é dispositivo móvel
is_mobile_device = is_mobile()

st.markdown("""
<style>
    .responsive-container {
        position: relative;
        overflow: hidden;
        padding-top: 75%; /* Proporção 4:3 */
    }
    
    .responsive-iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: 0;
    }
    
    @media (max-width: 768px) {
        .responsive-container {
            padding-top: 120%; /* Maior altura para mobile */
        }
    }
    
    .mobile-warning {
        background-color: #fff8e1;
        padding: 15px;
        border-radius: 5px;
        text-align: center;
        margin-bottom: 20px;
        border-left: 4px solid #ffc107;
    }
</style>
""", unsafe_allow_html=True)
# 4. Mostra cabeçalho
show_header(show_calculadora=False)
st.markdown("""
    <style>
        .mode-switcher a {
            transition: all 0.3s ease;
            font-weight: 500;
        }
        .mode-switcher a:hover {
            transform: scale(1.05);
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
=======
import streamlit.components.v1 as components
from utils import show_header, show_footer

# Configuração de layout
st.set_page_config(layout="wide", page_title="Dashboard de Resíduos")

# CSS para remover barra lateral e otimizar mobile
st.markdown("""
    <style>
        section[data-testid="stSidebar"] { display: none !important; }
        .stApp { padding: 0 !important; }
        iframe { border: none; }
        
        /* Container responsivo */
        .responsive-container {
            position: relative;
            overflow: hidden;
            padding-top: 56.25%; /* Proporção 16:9 */
        }
        
        .responsive-iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
        
        @media (max-width: 768px) {
            .responsive-container {
                padding-top: 100vh; /* Ocupa toda altura */
            }
>>>>>>> 308a06680915b6e125b8439cb7079b6483a8fa57
        }
    </style>
""", unsafe_allow_html=True)

<<<<<<< HEAD


# URL do Power BI
powerbi_link = "https://app.powerbi.com/view?r=eyJrIjoiYTE0NTliNjQtMTYzMC00MDZmLTgyODgtMTE5Y2UwOTc2MjQ2IiwidCI6ImU5YTgyZWM3LTRhODYtNDNkZS1hYjJhLTcxOWQ2Njk1OWExYiJ9"

# Parâmetros essenciais
powerbi_link += "&rs:embed=true"
powerbi_link += "&rs:command=Render"
powerbi_link += "&rs:device=desktop"
powerbi_link += "&rs:SuppressErrorRedirect=true"

# Verifica se é dispositivo móvel
is_mobile_device = is_mobile()

# Aviso para mobile
if is_mobile_device:
    st.markdown(
        '<div class="mobile-warning"> Para melhor experiência, gire seu dispositivo para o modo paisagem e use o modo claro</div>',
        unsafe_allow_html=True
    )


# HTML para incorporar o Power BI
st.markdown(f"""
<div class="responsive-container">
    <iframe class="responsive-iframe" 
            src="{powerbi_link}" 
            frameborder="0"
            allowFullScreen="true">
    </iframe>
</div>
""", unsafe_allow_html=True)

st.markdown("""
Você pode interagir com os gráficos, filtrar as informações por ano e material.
Para navegar pelas páginas da análise, basta clicar nos ícones disponíveis na barra lateral à esquerda.
""")

# Rodapé otimizado
show_footer()
=======
# Mostra cabeçalho
show_header(show_calculadora=False)

# URL do Power BI com parâmetros para forçar versão interativa
powerbi_link = "https://app.powerbi.com/view?r=eyJrIjoiYTE0NTliNjQtMTYzMC00MDZmLTgyODgtMTE5Y2UwOTc2MjQ2IiwidCI6ImU5YTgyZWM3LTRhODYtNDNkZS1hYjJhLTcxOWQ2Njk1OWExYiJ9"

# Adicione estes parâmetros essenciais:
powerbi_link += "&rs:embed=true"  # Força modo embed
powerbi_link += "&rs:command=Render"  # Força renderização completa
powerbi_link += "&rs:device=desktop"  # Força versão desktop

# Container responsivo
st.markdown(
    f"""
    <div class="responsive-container">
        <iframe class="responsive-iframe" 
                src="{powerbi_link}" 
                allowFullScreen="true">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)

# Rodapé
show_footer()
>>>>>>> 308a06680915b6e125b8439cb7079b6483a8fa57
