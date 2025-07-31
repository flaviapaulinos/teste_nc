import streamlit as st
from urllib.parse import urlencode, parse_qs

def is_mobile():
    """Determina se deve mostrar a versão mobile, considerando a preferência do usuário"""
    params = st.query_params.to_dict()
    
    if "force_mobile" in params:
        return True
    if "force_desktop" in params:
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

def get_page_url(page_path: str) -> str:
    """Gera URL para navegação entre páginas preservando parâmetros"""
    params = st.query_params.to_dict()
    
    # Remove parâmetros de controle de visualização
    params.pop("force_mobile", None)
    params.pop("force_desktop", None)
    
    # Constrói a query string
    query_string = urlencode(params, doseq=True)
    return f"?page={page_path}&{query_string}" if query_string else f"?page={page_path}"

def inject_custom_css():
    """Injeta CSS personalizado para remover estilos de link"""
    st.markdown(
        """
        <style>
            .nav-link-container a {
                color: inherit !important;
                text-decoration: none !important;
                font-weight: bold !important;
            }
            .nav-link-container a:hover {
                text-decoration: underline !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_header(show_calculadora=True):
    """Exibe o cabeçalho responsivo com navegação"""
    inject_custom_css()
    mobile_mode = is_mobile()
    
    # CSS para espaçamento e estilo dos links
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
            color: inherit;
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
                url1 = get_page_url("pages/Dashboard.py")
                st.markdown(
                    f'<div class="nav-link-container">'
                    f'<a href="{url1}">Análise Resíduos BH</a>'
                    f'</div>',
                    unsafe_allow_html=True
                )
            with col4:
                st.markdown(
                    '<div class="nav-link-container">'
                    '<a href="https://novocicloresiduos.com.br/">Sobre o Projeto</a>'
                    '</div>',
                    unsafe_allow_html=True
                )
            st.image("imagem/calc_mob.png", use_container_width=True)
        else:
            with col2:
                url = get_page_url("app.py")
                st.markdown(
                    f'<div class="nav-link-container">'
                    f'<a href="{url}">Calculadora de impacto coleta seletiva</a>'
                    f'</div>',
                    unsafe_allow_html=True
                )
            with col4:
                st.markdown(
                    '<div class="nav-link-container">'
                    '<a href="https://novocicloresiduos.com.br/">Sobre o Projeto</a>'
                    '</div>',
                    unsafe_allow_html=True
                )
    else:
        # DESKTOP
        st.image("imagem/header.png", use_container_width=True)
        
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        if show_calculadora:
            with col2:
                url1 = get_page_url("pages/Dashboard.py")
                st.markdown(
                    f'<div class="nav-link-container">'
                    f'<a href="{url1}">Análise Resíduos BH</a>'
                    f'</div>',
                    unsafe_allow_html=True
                )
            with col4:
                st.markdown(
                    '<div class="nav-link-container">'
                    '<a href="https://novocicloresiduos.com.br/">Sobre o Projeto</a>'
                    '</div>',
                    unsafe_allow_html=True
                )
            st.image("imagem/calc_bar.png", use_container_width=True)
        else:
            with col2:
                url = get_page_url("app.py")
                st.markdown(
                    f'<div class="nav-link-container">'
                    f'<a href="{url}">Calculadora de impacto coleta seletiva</a>'
                    f'</div>',
                    unsafe_allow_html=True
                )
            with col4:
                st.markdown(
                    '<div class="nav-link-container">'
                    '<a href="https://novocicloresiduos.com.br/">Sobre o Projeto</a>'
                    '</div>',
                    unsafe_allow_html=True
                )
        
        # Botão "visualize no celular" apenas para desktop
        with col1:
            if st.button("visualize no celular"):
                # Atualiza os parâmetros para forçar mobile
                new_params = st.query_params.to_dict()
                new_params["force_mobile"] = "true"
                if "force_desktop" in new_params:
                    del new_params["force_desktop"]
                st.query_params.clear()
                st.query_params.update(new_params)

def show_footer():
    """Exibe o rodapé com opções de visualização"""
    mobile_mode = is_mobile()
    
    if mobile_mode:
        st.image("imagem/logos_mob_fundo.png", use_container_width=True)
    else:
        st.image("imagem/logos.png", use_container_width=True)
    
    st.markdown("---")
    
    # Gera links com parâmetros preservados
    params = st.query_params.to_dict()
    
    # Link para versão mobile
    mobile_params = params.copy()
    mobile_params["force_mobile"] = "true"
    mobile_params.pop("force_desktop", None)
    mobile_query = urlencode(mobile_params, doseq=True)
    
    # Link para versão desktop
    desktop_params = params.copy()
    desktop_params["force_desktop"] = "true"
    desktop_params.pop("force_mobile", None)
    desktop_query = urlencode(desktop_params, doseq=True)
    
    # Link para reset
    reset_params = params.copy()
    reset_params.pop("force_mobile", None)
    reset_params.pop("force_desktop", None)
    reset_query = urlencode(reset_params, doseq=True)
    
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
    