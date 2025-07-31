import streamlit as st
<<<<<<< HEAD
from utils import show_header, show_footer, is_mobile 

# 1. DEVE SER O PRIMEIRO COMANDO: Configuração de layout responsivo
st.set_page_config(
    layout="wide",
    page_title="Calculadora de Impacto Ambiental",
    initial_sidebar_state="collapsed"
)

# 2. Detecta se é dispositivo móvel
is_mobile_device = is_mobile()

# CSS otimizado para dispositivos móveis
st.markdown("""
    <style>
        /* ... (seu CSS existente permanece igual) ... */
    </style>
""", unsafe_allow_html=True)

# Mostra cabeçalho
show_header(show_calculadora=True)

# === Dados e coeficientes ===
# Percentuais para coleta seletiva (quando o usuário recicla)
=======
from utils import show_header, show_footer


# Configuração de página com layout amplo
st.set_page_config(layout="wide", page_title="Calculadora de Impacto Ambiental")

st.markdown("""
    <style>
    @font-face {
        font-family: 'Avenir';
        src: local('Avenir'), url('https://fonts.cdnfonts.com/s/15335/AvenirLTStd-Roman.woff') format('woff');
        font-weight: normal;
        font-style: normal;
    }

    html, body, [class*="css"] {
        font-family: 'Avenir', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Mostra cabeçalho personalizado
show_header()

# === Dados e coeficientes ===
>>>>>>> 308a06680915b6e125b8439cb7079b6483a8fa57
percentual_coleta_seletiva = {
    'percentual_papel':  0.206745786,
    'percentual_plastico': 0.585485533,
    'percentual_metais': 0.104443029,
    'percentual_vidro': 0.112717273,
}

<<<<<<< HEAD
# Percentuais para coleta convencional (quando o usuário não recicla)
percentual_coleta_convencional = {
    'percentual_papel':  0.1529,
    'percentual_plastico': 0.14437,
    'percentual_metais': 0.0116,
    'percentual_vidro': 0.02918,
}

# Os demais coeficientes permanecem os mesmos
=======
>>>>>>> 308a06680915b6e125b8439cb7079b6483a8fa57
economia_energia = {
    'papel': 0.009720,
    'plastico': 0.005150,
    'metais': 0.040617,
    'vidro': 0.003180,
}

gee_evitada_tC02e = {
    'papel': 0.000270,
    'plastico': 0.001530,
    'metais': 0.001804,
    'vidro': 0.000250,
}

consumo_agua_evitado_m3 = {
    'papel': 0.040500,
    'plastico': 0.001950,
    'metais': 0.015700,
    'vidro': 0.001000,
}

area_monocultura_evitada_ha_ano = {
    'papel': 0.000014,
    'plastico': 0,
    'metais': 0.000001,
    'vidro': 0,
}

economia_com_insumos = {
    'papel': 0.330000,
    'plastico': 1.164000,
    'metais': 0.385800,
    'vidro': 0.120000,
}

beneficios_sociais = {
    'papel': 0.09194,
    'plastico': 0.11307,
    'metais': 0.09586,
    'vidro': 0.11252,
}

ipca_2010_2025 = 2.3452512

# === Pesos reais (em kg) ===
peso_sacola_coleta_seletiva = 1
peso_saco_30l_seletiva = 3.5
peso_sacola_convencional = 1.75
peso_saco_30l_convencional = 7.5

# === Função principal de cálculo ===
def calcular_impactos(kg_total, percentual):
    impactos = {
        "Energia economizada (R$)": 0,
        "GEE evitado (tCO₂e)": 0,
        "Água evitada (m³)": 0,
        "Área de monocultura evitada (ha/ano)": 0,
        "Economia com insumos (R$)": 0,
        "Benefícios sociais(R$)": 0,
    }

    materiais = ['papel', 'plastico', 'metais', 'vidro']
    for material in materiais:
        chave_percentual = f'percentual_{material}'
        frac = percentual.get(chave_percentual, 0)
        qtd_kg = kg_total * frac

        impactos["Energia economizada (R$)"] += qtd_kg * economia_energia[material] * ipca_2010_2025
        impactos["GEE evitado (tCO₂e)"] += qtd_kg * gee_evitada_tC02e[material]
        impactos["Água evitada (m³)"] += qtd_kg * consumo_agua_evitado_m3[material]
<<<<<<< HEAD
        impactos["Área de monocultura evitada (ha/ano)"] += qtd_kg * area_monocultura_evitada_ha_ano[material] * 10000
=======
        impactos["Área de monocultura evitada (ha/ano)"] += qtd_kg * area_monocultura_evitada_ha_ano[material]*10000
>>>>>>> 308a06680915b6e125b8439cb7079b6483a8fa57
        impactos["Economia com insumos (R$)"] += qtd_kg * economia_com_insumos[material] * ipca_2010_2025
        impactos["Benefícios sociais(R$)"] += qtd_kg * beneficios_sociais[material] * ipca_2010_2025

    resultados_formatados = {
        "Economia com insumos: R$": f"{impactos['Economia com insumos (R$)']:.2f}",
        "Benefícios sociais gerados: R$": f"{impactos['Benefícios sociais(R$)']:.2f}", 
        "Energia economizada: R$": f"{impactos['Energia economizada (R$)']:.2f}",
        "Gases do efeito estufa evitados:": f"{impactos['GEE evitado (tCO₂e)']:.4f} tCO₂e",
        "Consumo de água evitado:": f"{impactos['Água evitada (m³)']:.2f} m³",
        "Área destinada a monocultura evitada:": f"{impactos['Área de monocultura evitada (ha/ano)']:.2f} m²/ano",   
    }

    return resultados_formatados

# === Container central para calculadora expandida ===
with st.container():
<<<<<<< HEAD

        # Adiciona o container principal responsivo
        st.markdown("""
        <div class="main-container">
    """, unsafe_allow_html=True)

        st.markdown("""
<div style='text-align: center; background-color:#f0f2f6; padding:15px; border-radius:5px; margin-top:5px;'>
Quando a indústria utiliza materiais reciclados, menos árvores, animais e rios são impactados. Esses benefícios são imensos e não podem ser expressos em números; <strong> mas alguns benefícios econômicos, sociais e ambientais podem ser expressos em números.</strong>
=======
        st.markdown("""


<div style='text-align: center; background-color:#f0f2f6; padding:15px; border-radius:5px; margin-top:5px;'>
Quando a indústria utiliza materiais reciclados, menos árvores, animais e rios são impactados. Esses benefícios são imensos e não têm como ser expressos em números. <strong>Alguns benefícios econômicos, sociais e ambientais podem ser expressos em números!</strong>
>>>>>>> 308a06680915b6e125b8439cb7079b6483a8fa57
</div>
""", unsafe_allow_html=True)
        st.markdown(" ")
        # Imagem floresta
        st.image("imagem/faixa_1.PNG", use_container_width=True)
        st.subheader("♻️ Descubra Alguns Impactos da Sua Reciclagem")
        
        # Usando 2 colunas com mais espaço
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**✅ Você recicla?**")
            st.markdown("Informe quantos **sacos e/ou sacolas você destina para a coleta seletiva** por semana:")
            sacolas_recicla = st.number_input("Sacolas de supermercado", min_value=0, step=1, key="sacolas_recicla")
<<<<<<< HEAD
            sacos30_recicla = st.number_input("Sacos 30 litros", min_value=0, step=1, key="sacos30_recicla")
=======
            sacos30_recicla = st.number_input("Sacos 30L", min_value=0, step=1, key="sacos30_recicla")
>>>>>>> 308a06680915b6e125b8439cb7079b6483a8fa57
        
        with col2:
            st.markdown("**🚫 Você ainda não recicla?**")
            st.markdown("Informe quantos **sacos e/ou sacolas você destina para a coleta de lixo por semana:**")
            sacolas_nao_recicla = st.number_input("Sacolas de supermercado com lixo convencional", min_value=0, step=1, key="sacolas_nao_recicla")
<<<<<<< HEAD
            sacos30_nao_recicla = st.number_input("Sacos 30 litros com lixo convencional", min_value=0, step=1, key="sacos30_nao_recicla")
        
        # === Peso total (em kg por ano - 52 semanas) ===
        kg_recicla = (sacolas_recicla * peso_sacola_coleta_seletiva + sacos30_recicla * peso_saco_30l_seletiva) * 52
        kg_nao_recicla = (sacolas_nao_recicla * peso_sacola_convencional + sacos30_nao_recicla * peso_saco_30l_convencional) * 52

        # === Validação e cálculo ===
        if kg_recicla > 0 and kg_nao_recicla > 0:
            st.warning("⚠️ Apenas uma opção por vez: '✅ Você recicla?' ou '🚫 Você ainda não recicla?' ")
        elif kg_recicla > 0:
            # Usa percentuais de coleta seletiva para quem recicla
=======
            sacos30_nao_recicla = st.number_input("Sacos 30L com lixo convencional", min_value=0, step=1, key="sacos30_nao_recicla")
        
        # === Peso total (em kg por ano - 52 semanas) ===
        kg_recicla = (sacolas_recicla * peso_sacola_coleta_seletiva + sacos30_recicla * peso_saco_30l_seletiva) * 52.1786
        kg_nao_recicla = (sacolas_nao_recicla * peso_sacola_convencional + sacos30_nao_recicla * peso_saco_30l_convencional) * 52.1786

    
        
        # === Validação e cálculo ===
        if kg_recicla > 0 and kg_nao_recicla > 0:
            st.warning("⚠️ Preencha apenas um dos lados")
        elif kg_recicla > 0:
>>>>>>> 308a06680915b6e125b8439cb7079b6483a8fa57
            impactos = calcular_impactos(kg_recicla, percentual_coleta_seletiva)
            st.markdown("---")
            st.subheader("🌱 Impacto positivo gerado pela sua reciclagem em um ano:")
          
<<<<<<< HEAD
            # Mostrar resultados em colunas
=======
                       
            # Mostrar resultados em colunas para melhor visualização
>>>>>>> 308a06680915b6e125b8439cb7079b6483a8fa57
            cols = st.columns(2)
            items = list(impactos.items())
            for i, (k, v) in enumerate(items):
                with cols[i % 2]:
                    st.markdown(f"<div style='padding:10px; border-radius:10px; background-color:#f0f8ff; margin-bottom:10px;'>"
                                f"<b>{k}</b> {v}</div>", 
                                unsafe_allow_html=True)
            st.markdown("""
<<<<<<< HEAD
<div style='background-color:#f0f2f6; padding:15px; border-radius:5px; margin-top:5px;'>
<strong> Imagine o impacto, se todos os habitantes de Belo Horizonte destinassem corretamente seus resíduos recicláveis!</strong>
*Fonte: Pesquisa sobre Pagamento por Serviços Ambientais Urbanos para Gestão de Resíduos Sólidos, elaborada pelo Instituto de Pesquisa Econômica Aplicada (IPEA, 2010).<br>
=======


<div style='background-color:#f0f2f6; padding:15px; border-radius:5px; margin-top:5px;'>

*Fonte: Pesquisa sobre Pagamento por Serviços Ambientais Urbanos para Gestão de Resíduos Sólidos, elaborada pelo Instituto de Pesquisa Econômica Aplicada (IPEA, 2010).<br>

>>>>>>> 308a06680915b6e125b8439cb7079b6483a8fa57
*Valores corrigidos pelo IPCA
</div>
""", unsafe_allow_html=True)       
        elif kg_nao_recicla > 0:
<<<<<<< HEAD
            # Usa percentuais de coleta convencional para quem não recicla
            impactos = calcular_impactos(kg_nao_recicla, percentual_coleta_convencional)
=======
            impactos = calcular_impactos(kg_nao_recicla, percentual_coleta_seletiva)
>>>>>>> 308a06680915b6e125b8439cb7079b6483a8fa57
            st.markdown("---")
            
            st.subheader("🚮 Impacto positivo que você está **deixando de gerar** em um ano:")
        
<<<<<<< HEAD
=======
            
>>>>>>> 308a06680915b6e125b8439cb7079b6483a8fa57
            # Mostrar resultados em colunas
            cols = st.columns(2)
            items = list(impactos.items())
            for i, (k, v) in enumerate(items):
                with cols[i % 2]:
                    st.markdown(f"<div style='padding:10px; border-radius:10px; background-color:#fff0f0; margin-bottom:10px;'>"
                                f"<b>{k}</b> {v}</div>", 
                                unsafe_allow_html=True)
            
            st.markdown("""
<<<<<<< HEAD
<div style='background-color:#f0f2f6; padding:15px; border-radius:5px; margin-top:20px;'>
<strong> Imagine o impacto se todos os habitantes de Belo Horizonte destinassem corretamente seus resíduos recicláveis!</strong>
*Fonte: Pesquisa sobre Pagamento por Serviços Ambientais Urbanos para Gestão de Resíduos Sólidos, elaborada pelo Instituto de Pesquisa Econômica Aplicada (IPEA, 2010).<br>
=======


<div style='background-color:#f0f2f6; padding:15px; border-radius:10px; margin-top:20px;'>

*Fonte: Pesquisa sobre Pagamento por Serviços Ambientais Urbanos para Gestão de Resíduos Sólidos, elaborada pelo Instituto de Pesquisa Econômica Aplicada (IPEA, 2010).<br>

>>>>>>> 308a06680915b6e125b8439cb7079b6483a8fa57
*Valores corrigidos pelo IPCA
</div>
""", unsafe_allow_html=True)

<<<<<<< HEAD
        st.markdown("</div>", unsafe_allow_html=True)

# Rodapé
=======
# === Rodapé ===
>>>>>>> 308a06680915b6e125b8439cb7079b6483a8fa57
show_footer()