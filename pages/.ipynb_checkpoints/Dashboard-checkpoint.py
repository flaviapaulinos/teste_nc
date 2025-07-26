import streamlit as st
import streamlit.components.v1 as components
from utils import show_header, show_footer

# Configuração de layout amplo
st.set_page_config(layout="wide")

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