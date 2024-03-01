import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#Importar logo
im = Image.open(r'logo.png')
im2 = Image.open(r'foguete.png')

# Define as cores da página
st.set_page_config(
    page_title='Simulador G10 e S10',
    page_icon=im,
    layout='wide'
)

with open(r'style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown('<div style="position: fixed; bottom: 0; right: 196px;"><p style="color: white;"><span style="color:black;font-size: 20px;font-family: Barlow Semibold;">MADE BY </span><span style="color:#9966FF;font-size: 20px; font-family: Barlow Semibold, sans-serif;">PERFORMANCE</span></p></div>', unsafe_allow_html=True)
st.markdown('<div style="position: fixed; bottom: 0; left: 374px;"><p style="color: grey; font-size: 14px;font-family: Barlow;">Criado por Lucas Silva</p></div>', unsafe_allow_html=True)

vazio2, col1, col2, vazio = st.columns([9, 1, 19, 9])

with col1:
    st.write('')
    st.image(im2, width=32)

with col2:
    st.title('Simulador G10 e S10')

#st.title('Simulador G10 e S10')


st.write("<div style='text-align: center;'> <span style='font-family: Barlow; font-size: 16px;'>Este aplicativo faz uma simulação da posição no ranking do próximo mês com base nos preenchimentos do usuário.</span> </div>", unsafe_allow_html=True)

# Título do aplicativo
# st.title('Simulador G10 e S10')

# Descrição do aplicativo
# st.write("<div style='text-align: center;'> <span style='font-family: Barlow; font-size: 16px;'>Este aplicativo faz uma simulação da posição no ranking do próximo mês com base nos preenchimentos do usuário.</span> </div>", unsafe_allow_html=True)

def link():
    st.sidebar.markdown("<a href='https://madebyperformance-simuladorlider-lider-mxv3v4.streamlit.app/' target='_blank' style='text-decoration: none; font-family: Barlow; font-weight: bold; font-size: 22px; color: white;'>SIMULADOR PARTNERSHIP</a>", unsafe_allow_html=True)
    st.sidebar.markdown("<span style='font-family: Barlow; color: white; font-size: 14px;'>Clique acima para ser redirecionado ao Simulador do Partnership Líder 2023.</span>", unsafe_allow_html=True)
    
link()

# Remover o menu

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

df = pd.read_excel(r'Base_Simulador.xlsx')
df['KPI6'] = df['KPI6'].astype(int)
df['KPI1'] = df['KPI1'].astype(int)

# Input widgets
categoria = st.radio('Categoria', ('G10', 'S10'))
st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Você selecionou a categoria {categoria}.</span>", unsafe_allow_html=True)

posicao = st.number_input('Posição no último ranking', step=int(1))
fxp0="{:.0f}".format(posicao) 
st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Você selecionou a {fxp0}ª posição.</span>", unsafe_allow_html=True)

faturamento = st.number_input('Faturamento esperado no mês', step=int(1))
fxp1="{:,.0f}".format(faturamento) 
fxp1 = fxp1.replace(",",".")
st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Você selecionou um faturamento de R$ {fxp1}.</span>", unsafe_allow_html=True)

incremento = st.number_input('Incremento de PL esperado no mês', step=int(1))
fxp2="{:,.0f}".format(incremento) 
fxp2 = fxp2.replace(",",".")
st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Você selecionou um incremento de PL de R$ {fxp2}.</span>", unsafe_allow_html=True)

objetivo = st.number_input('Objetivo alcançado no mês', step=int(1))
fxp3="{:.0f}".format(objetivo) 
st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Você selecionou um objetivo de {fxp3} %.</span>", unsafe_allow_html=True)


categoria = 'G10'
posicao = 17
faturamento = 4000000
incremento = 60000000
objetivo = 150

# Calcular nova posição

if st.button('Calcular nova posição'):
    if posicao == 0:
      st.write("<span style='font-family: Barlow; color: rgb(255, 0, 0);font-size: 20px;'>Por favor, insira sua posição atual para começar a simulação.</span>", unsafe_allow_html=True) 
    if posicao > 0:

        q1 = df['KPI6'].max()
        q1 = q1 + 1
    
        if categoria == 'G10':
                df_g10 = df[df['KPI2'] == 'G10']
                
                df_g10['KPI44'] = (df_g10['KPI4']) / q1
                df_g10['KPI44'] = df_g10['KPI4'] +  df_g10['KPI44']
                
                df_g10['KPI33'] = (df_g10['KPI3']) / q1
                df_g10['KPI33'] = df_g10['KPI3'] + df_g10['KPI33']
              
                df_g10.loc[df_g10['KPI1'] == posicao, 'KPI44'] = df_g10.loc[df_g10['KPI1'] == posicao, 'KPI4'] + faturamento
                df_g10.loc[df_g10['KPI1'] == posicao, 'KPI33'] = df_g10.loc[df_g10['KPI1'] == posicao, 'KPI3'] + incremento
                df_g10.loc[df_g10['KPI1'] == posicao, 'KPI5'] = objetivo / 100

                Valor_minimo_incremento_G10 = df_g10['KPI33'].min()
                Valor_maximo_incremento_G10 = df_g10['KPI33'].max()

                Valor_minimo_fat_G10 = df_g10['KPI44'].min()
                Valor_maximo_fat_G10 = df_g10['KPI44'].max()

                Valor_minimo_atingimento_G10 = df_g10['KPI5'].min()
                Valor_maximo_atingimento_G10 = df_g10['KPI5'].max()

                # Aplicando a fórmula
                df_g10['KPI333'] = ((df_g10['KPI33'] - Valor_minimo_incremento_G10) / (Valor_maximo_incremento_G10 - Valor_minimo_incremento_G10) * 2 - 1 + 1) * 100
                df_g10['KPI444'] = ((df_g10['KPI44'] - Valor_minimo_fat_G10) / (Valor_maximo_fat_G10 - Valor_minimo_fat_G10) * 2 - 1 + 1) * 100
                df_g10['KPI555'] = ((df_g10['KPI5'] - Valor_minimo_atingimento_G10) / (Valor_maximo_atingimento_G10 - Valor_minimo_atingimento_G10) * 2 - 1 + 1) * 100
                df_g10['KPI6666'] = df_g10['KPI44']/10000000
                
                # pesos G10
                P_fat_G10 = 0.4
                P_inc_G10 = 0.3
                P_ating_G10 = 0.3

                # Calculando o score
                df_g10['KPI1212'] = (df_g10['KPI444'] * P_fat_G10) + (df_g10['KPI333'] * P_inc_G10) + (df_g10['KPI555'] * P_ating_G10) + (df_g10['KPI6666'])
                df_g10['KPI1313'] = df_g10['KPI1212'].rank(ascending=False)
                df_g10 = df_g10.sort_values(by='KPI1313', ascending=True)
                
                df_g10['KPI1313'] = df_g10['KPI1313'].astype(int)
                df_g10['KPI1'] = df_g10['KPI1'].astype(int)
                
                ranking_antigo_g10 = df_g10.loc[df_g10['KPI1'] == posicao, 'KPI1'].iloc[0]
                ranking_novo_g10 = df_g10.loc[df_g10['KPI1'] == posicao, 'KPI1313'].iloc[0]
                
 
                if ranking_novo_g10 <= 10:
                    if posicao > 10:
                        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Com base nos valores preenchidos e considerando que as demais equipes/filiais continuarão no mesmo ritmo, você passaria a ocupar a {ranking_novo_g10}ª posição, entrando no {categoria}. Parabéns!</span>", unsafe_allow_html=True)
                    if posicao <= 10:
                        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Com base nos valores preenchidos e considerando que as demais equipes/filiais continuarão no mesmo ritmo, você passaria a ocupar a {ranking_novo_g10}ª posição, permanecendo no {categoria}. Parabéns!</span>", unsafe_allow_html=True)
                if ranking_novo_g10 > 10:
                    if posicao > 10:
                        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Com base nos valores preenchidos e considerando que as demais equipes/filiais continuarão no mesmo ritmo, você passaria a ocupar a {ranking_novo_g10}ª posição, permanecendo fora do {categoria}.</span>", unsafe_allow_html=True)
                    if posicao <= 10:
                        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Com base nos valores preenchidos e considerando que as demais equipes/filiais continuarão no mesmo ritmo, você passaria a ocupar a {ranking_novo_g10}ª posição, saindo do {categoria}. Cuidado!</span>", unsafe_allow_html=True)
          
          
        if categoria == 'S10':
                df_s10 = df[df['KPI2'] == 'G10']
                
                df_s10['KPI44'] = (df_s10['KPI4']) / q1
                df_s10['KPI44'] = df_s10['KPI4'] + df_s10['KPI44']
                
                df_s10['KPI33'] = (df_s10['KPI3']) / q1
                df_s10['KPI33'] = df_s10['KPI3'] + df_s10['KPI33']
              
                df_s10.loc[df_s10['KPI1'] == posicao, 'KPI44'] = df_s10.loc[df_s10['KPI1'] == posicao, 'KPI4'] + faturamento
                df_s10.loc[df_s10['KPI1'] == posicao, 'KPI33'] = df_s10.loc[df_s10['KPI1'] == posicao, 'KPI3'] + incremento
                df_s10.loc[df_s10['KPI1'] == posicao, 'KPI5'] = objetivo / 100
                
                
                
                Valor_minimo_incremento_S10 = df_s10['KPI33'].min()
                Valor_maximo_incremento_S10 = df_s10['KPI33'].max()

                Valor_minimo_fat_S10 = df_s10['KPI44'].min()
                Valor_maximo_fat_S10 = df_s10['KPI44'].max()

                Valor_minimo_atingimento_S10 = df_s10['KPI55'].min()
                Valor_maximo_atingimento_S10 = df_s10['KPI55'].max()

                # Aplicando a fórmula
                df_s10['KPI333'] = ((df_s10['KPI33'] - Valor_minimo_incremento_S10) / (Valor_maximo_incremento_S10 - Valor_minimo_incremento_S10) * 2 - 1 + 1) * 100
                df_s10['KPI444'] = ((df_s10['KPI44'] - Valor_minimo_fat_S10) / (Valor_maximo_fat_S10 - Valor_minimo_fat_S10) * 2 - 1 + 1) * 100
                df_s10['KPI555'] = ((df_s10['KPI55'] - Valor_minimo_atingimento_S10) / (Valor_maximo_atingimento_S10 - Valor_minimo_atingimento_S10) * 2 - 1 + 1) * 100
                
                # pesos S10
                P_fat_S10 = 0.2
                P_inc_S10 = 0.5
                P_ating_S10 = 0.3

                # Calculando o score
                df_s10['KPI1212'] = (df_s10['KPI44'] * P_fat_S10) + (df_s10['KPI33'] * P_inc_S10) + (df_s10['KPI55'] * P_ating_S10)
                df_s10['KPI1313'] = df_s10['KPI1212'].rank(ascending=False)
                
                df_s10 = df_s10.sort_values(by='KPI1313', ascending=True)
                
                df_s10['KPI1313'] = df_s10['KPI1313'].astype(int)
                df_s10['KPI1'] = df_s10['KPI1'].astype(int)
                
                ranking_antigo_s10 = df_s10.loc[df_s10['KPI1'] == posicao, 'KPI1'].loc[0]
                ranking_novo_s10 = df_s10.loc[df_s10['KPI1'] == posicao, 'KPI1313'].loc[0]

                if ranking_novo_s10 <= 10:
                    if posicao > 10:
                        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Com base nos valores preenchidos e considerando que as demais equipes/filiais continuarão no mesmo ritmo, você passaria a ocupar a {ranking_novo_s10}ª posição, entrando no {categoria}. Parabéns!</span>", unsafe_allow_html=True)
                    if posicao <= 10:
                        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Com base nos valores preenchidos e considerando que as demais equipes/filiais continuarão no mesmo ritmo, você passaria a ocupar a {ranking_novo_s10}ª posição, permanecendo no {categoria}. Parabéns!</span>", unsafe_allow_html=True)
                if ranking_novo_s10 > 10:
                    if posicao > 10:
                        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Com base nos valores preenchidos e considerando que as demais equipes/filiais continuarão no mesmo ritmo, você passaria a ocupar a {ranking_novo_s10}ª posição, permanecendo fora do {categoria}.</span>", unsafe_allow_html=True)
                    if posicao <= 10:
                        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Com base nos valores preenchidos e considerando que as demais equipes/filiais continuarão no mesmo ritmo, você passaria a ocupar a {ranking_novo_s10}ª posição, saindo do {categoria}. Cuidado!</span>", unsafe_allow_html=True)
