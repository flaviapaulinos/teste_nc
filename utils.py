import streamlit as st
<<<<<<< HEAD
import os
from urllib.parse import urlencode

def is_mobile():
    """Determina se deve mostrar a versão mobile, considerando a preferência do usuário"""
    if "force_mobile" in st.query_params:
        return True
    if "force_desktop" in st.query_params:
        return False
    
    try:
        ctx = st.runtime.scriptrunner.script_run_context.get_script_run_ctx()
        if ctx and hasattr(ctx, 'request'):
            user_agent = ctx.request.headers.get("User-Agent", "").lower()
            mobile_keywords = ['mobile', 'android', 'iphone', 'ipad', 'windows phone']
            return any(keyword in user_agent for keyword in mobile_keywords)
    except Exception:
        pass
    return False

def get_page_url(page_path):
    """Gera URL da página com parâmetros atuais preservados"""
    params = st.query_params.to_dict()
    
    # Remove parâmetros de controle se existirem
    if "force_mobile" in params:
        del params["force_mobile"]
    if "force_desktop" in params:
        del params["force_desktop"]
        
    query_string = urlencode(params)
    return f"{page_path}?{query_string}" if query_string else page_path

def show_header(show_calculadora=True):
    mobile_mode = is_mobile()
    
    # Adiciona CSS para espaçamento dos links
    st.markdown("""
    <style>
        .nav-link-container {
            padding: 0 15px;
            margin-bottom: 10px;
            text-align: center;
        }
        
        @media (max-width: 768px) {
            .nav-link-container {
                padding: 0 5px;
            }
        }
        
        .nav-link {
            display: block;
            padding: 8px 12px;
            border-radius: 4px;
            transition: background-color 0.3s;
            text-decoration: none;
            color: inherit;
            font-weight: bold;
        }
        .nav-link:hover {
            background-color: #f0f0f0;
        }
    </style>
    """, unsafe_allow_html=True)
    
    if mobile_mode:
        st.image("imagem/header_mob.png", use_container_width=True)
        
        col1, col2, col3, col4 = st.columns([1, 2, 1, 2])
        if show_calculadora:
            with col2:
                url = get_page_url("pages/Dashboard.py")
                st.markdown(
                    f'<div class="nav-link-container">'
                    f'<a href="{url}" class="nav-link">Análise Resíduos BH</a>'
                    f'</div>',
                    unsafe_allow_html=True
                )
            with col4:
                st.markdown(
                    '<div class="nav-link-container">'
                    '<a href="https://novocicloresiduos.com.br/" class="nav-link">Sobre o Projeto</a>'
                    '</div>',
                    unsafe_allow_html=True
                )
            st.image("imagem/calc_mob.png", use_container_width=True)
        else:
            with col2:
                url = get_page_url("app.py")
                st.markdown(
                    f'<div class="nav-link-container">'
                    f'<a href="{url}" class="nav-link">Calculadora de impacto coleta seletiva</a>'
                    f'</div>',
                    unsafe_allow_html=True
                )
            with col4:
                st.markdown(
                    '<div class="nav-link-container">'
                    '<a href="https://novocicloresiduos.com.br/" class="nav-link">Sobre o Projeto</a>'
                    '</div>',
                    unsafe_allow_html=True
                )
    else:
        st.image("imagem/header.png", use_container_width=True)
        
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        if show_calculadora:
            with col2:
                url = get_page_url("pages/Dashboard.py")
                st.markdown(
                    f'<a href="{url}" class="nav-link">Análise Resíduos BH</a>',
                    unsafe_allow_html=True
                )
            with col4:
                st.markdown(
                    '<a href="https://novocicloresiduos.com.br/" class="nav-link">Sobre o Projeto</a>',
                    unsafe_allow_html=True
                )
            st.image("imagem/calc_bar.png", use_container_width=True)
        else:
            with col2:
                url = get_page_url("app.py")
                st.markdown(
                    f'<a href="{url}" class="nav-link">Calculadora de impacto coleta seletiva</a>',
                    unsafe_allow_html=True
                )
            with col4:
                st.markdown(
                    '<a href="https://novocicloresiduos.com.br/" class="nav-link">Sobre o Projeto</a>',
                    unsafe_allow_html=True
                )

def show_footer():
    if is_mobile():
        st.image("imagem/logos_mob_fundo.png", use_container_width=True)
    else:
        st.image("imagem/logos.png", use_container_width=True)
    
    st.markdown("---")
    
    # Gera links com parâmetros preservados
    params = st.query_params.to_dict()
    
    # Link para versão mobile
    mobile_params = params.copy()
    mobile_params["force_mobile"] = "1"
    if "force_desktop" in mobile_params:
        del mobile_params["force_desktop"]
    mobile_query = urlencode(mobile_params)
    
    # Link para versão desktop
    desktop_params = params.copy()
    desktop_params["force_desktop"] = "1"
    if "force_mobile" in desktop_params:
        del desktop_params["force_mobile"]
    desktop_query = urlencode(desktop_params)
    
    # Link para reset
    reset_params = params.copy()
    if "force_mobile" in reset_params:
        del reset_params["force_mobile"]
    if "force_desktop" in reset_params:
        del reset_params["force_desktop"]
    reset_query = urlencode(reset_params)
    
    st.markdown(f"""
    <div style="text-align: center; margin: 20px 0;">
        <a href="?{mobile_query}" style="display: inline-block; padding: 12px 20px; background-color: #4CAF50; color: white; border-radius: 4px; text-decoration: none; margin: 0 10px;">
            Versão Celular
        </a>
        <a href="?{desktop_query}" style="display: inline-block; padding: 12px 20px; background-color: #2196F3; color: white; border-radius: 4px; text-decoration: none; margin: 0 10px;">
            Versão Desktop
        </a>
    </div>
    <div style="text-align: center; margin-top: 10px;">
        <small><a href="?{reset_query}" style="color: #666; text-decoration: none;">Restaurar modo padrão</a></small>
    </div>
    """, unsafe_allow_html=True)
=======

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
>>>>>>> 308a06680915b6e125b8439cb7079b6483a8fa57
