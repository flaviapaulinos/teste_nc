import streamlit as st
import streamlit.components.v1 as components
from utils import show_header, show_footer

# Configuração de layout amplo
st.set_page_config(layout="wide")

<<<<<<< HEAD
# === ADICIONE AQUI O CSS PARA REMOVER A BARRA LATERAL ===
st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        .block-container {
            padding-top: 2rem;
            max-width: 100% !important;
            padding-left: 5%;
            padding-right: 5%;
        }
        header {
            max-width: 100% !important;
            left: 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

=======
>>>>>>> 308a06680915b6e125b8439cb7079b6483a8fa57
# Mostra cabeçalho personalizado
show_header(show_calculadora=False)

# Container central para conteúdo
with st.container():

    # Link do Power BI
    powerbi_link = "https://app.powerbi.com/view?r=eyJrIjoiYTE0NTliNjQtMTYzMC00MDZmLTgyODgtMTE5Y2UwOTc2MjQ2IiwidCI6ImU5YTgyZWM3LTRhODYtNDNkZS1hYjJhLTcxOWQ2Njk1OWExYiJ9"

    st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <iframe title="PowerBI" width="100%" height="561" src="{powerbi_link}" frameborder="0" allowFullScreen="true"></iframe>
    </div>
    """,
    unsafe_allow_html=True
)
        

# Rodapé
show_footer()