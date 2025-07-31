import streamlit as st
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
        }
    </style>
""", unsafe_allow_html=True)



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