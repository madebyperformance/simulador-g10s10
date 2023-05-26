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

st.markdown('<div style="position: fixed; bottom: 0; right: 100px;"><p style="color: white;"><span style="color:black;font-size: 20px;font-family: Barlow Semibold;">MADE BY </span><span style="color:#9966FF;font-size: 20px; font-family: Barlow Semibold, sans-serif;">PERFORMANCE</span></p></div>', unsafe_allow_html=True)
st.markdown('<div style="position: fixed; bottom: 0; right: 1324px;"><p style="color: grey; font-size: 14px;font-family: Barlow;">Criado por Letícia Rodrigues</p></div>', unsafe_allow_html=True)

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

df = pd.read_excel(r'Base Simulador.xlsx')
df = df.drop(columns=['Unnamed: 0'])

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
saldo = st.number_input('Saldo de HC esperado no mês', step=int(1))
fxp3="{:.0f}".format(saldo) 
if saldo > 0:
    if saldo == 1:
        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Sua previsão é de {fxp3} assessor entrando no mês.</span>", unsafe_allow_html=True)
    else:
         st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Sua previsão é de {fxp3} assessores entrando no mês.</span>", unsafe_allow_html=True)
elif saldo < 0:
    saldoadaptado = saldo * -1
    fxp3="{:.0f}".format(saldoadaptado)
    if saldo == -1:
        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Sua previsão é de {fxp3} assessor saindo no mês.</span>", unsafe_allow_html=True)
    else:
         st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Sua previsão é de {fxp3} assessores saindo no mês.</span>", unsafe_allow_html=True)
else:
    st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Sua previsão é de nenhum assessor entrando ou saindo no mês.</span>", unsafe_allow_html=True)

# Calcular nova posição

if st.button('Calcular previsão de posição'):

    if posicao <= 0:
        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: red;'>A posição não pode ser menor ou igual a 0.</span>", unsafe_allow_html=True)
    else:
        q1 = df['KPI7'].mean()
        q2 = q1 + 1

        if categoria == 'G10':
                df_g10 = df[df['KPI9'] == 'G10']
                #previsao de fat (media * n)
                df_g10['KPI1'] = (df_g10['KPI1'] / q1) * q2
                #previsao de hc (media * n)
                df_g10['KPI3'] = (df_g10['KPI3'] / q1) * q2
                #previsao de inc (media * n)
                df_g10['KPI4'] = (df_g10['KPI4'] / q1) * q2
                #previsao de pl (ultimo pl + media incremento)
                df_g10['KPI8'] = df_g10['KPI8'] + (df_g10['KPI4'] / q2)
                #running fat (previsao fat / metas fat)
                df_g10['KPI10'] = df_g10['KPI1'] / df_g10['KPI2']
                #running pl (previsao pl / meta pl)
                df_g10['KPI11'] = df_g10['KPI8'] / df_g10['KPI6']

                df_g10['KPI1'] = np.where(df_g10['KPI5'] == posicao, (((df_g10['KPI1'] / q2) * q1) + faturamento), df_g10['KPI1'])
                df_g10['KPI3'] = np.where(df_g10['KPI5'] == posicao, (((df_g10['KPI3'] / q2) * q1) + saldo), df_g10['KPI3'])
                df_g10['KPI8'] = np.where(df_g10['KPI5'] == posicao, ((df_g10['KPI8'] - (df_g10['KPI4'] / q2)) + incremento), df_g10['KPI8'])
                df_g10['KPI4'] = np.where(df_g10['KPI5'] == posicao, (((df_g10['KPI4'] / q2) * q1) + incremento), df_g10['KPI4'])
                df_g10['KPI10'] = np.where(df_g10['KPI5'] == posicao, (df_g10['KPI1'] / df_g10['KPI2']), df_g10['KPI10'])
                df_g10['KPI11'] = np.where(df_g10['KPI5'] == posicao, (df_g10['KPI8'] / df_g10['KPI6']), df_g10['KPI11'])

                df_g10['KPI111'] = df_g10['KPI1'].rank(ascending=True)
                df_g10['KPI1010'] = df_g10['KPI10'].rank(ascending=True)
                df_g10['KPI44'] = df_g10['KPI4'].rank(ascending=True)
                df_g10['KPI1111'] = df_g10['KPI11'].rank(ascending=True)
                df_g10['KPI33'] = df_g10['KPI3'].rank(ascending=True)

                p1 = 0.3
                p10 = 0.3
                p4 = 0.15
                p11 = 0.15
                p3 = 0.1

                df_g10['KPI12'] = (p1 * df_g10['KPI111']) + (p10 * df_g10['KPI1010']) + (p3 * df_g10['KPI33']) + (p4 * df_g10['KPI44']) + (p11 * df_g10['KPI1111'])
                df_g10['KPI13'] = df_g10['KPI12'].rank(ascending=False)

                new_p = df_g10.loc[df_g10['KPI5'] == posicao]
                new_p = pd.DataFrame(new_p)
                column = new_p.columns.get_loc('KPI13')
                new_p = new_p.iloc[0,column]
                new_p = new_p.astype(int).round(0)

                if new_p <= 10:
                    if posicao > 10:
                        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Com base nos valores preenchidos e considerando que as demais equipes/filiais continuarão no mesmo ritmo, você passaria a ocupar a {new_p}ª posição, entrando no {categoria}. Parabéns!</span>", unsafe_allow_html=True)
                    if posicao <= 10:
                        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Com base nos valores preenchidos e considerando que as demais equipes/filiais continuarão no mesmo ritmo, você passaria a ocupar a {new_p}ª posição, permanecendo no {categoria}. Parabéns!</span>", unsafe_allow_html=True)
                if new_p > 10:
                    if posicao > 10:
                        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Com base nos valores preenchidos e considerando que as demais equipes/filiais continuarão no mesmo ritmo, você passaria a ocupar a {new_p}ª posição, permanecendo fora do {categoria}.</span>", unsafe_allow_html=True)
                    if posicao <= 10:
                        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Com base nos valores preenchidos e considerando que as demais equipes/filiais continuarão no mesmo ritmo, você passaria a ocupar a {new_p}ª posição, saindo do {categoria}. Cuidado!</span>", unsafe_allow_html=True)

        if categoria == 'S10':
                df_s10 = df[df['KPI9'] == 'S10']
                #previsao de fat (media * n)
                df_s10['KPI1'] = (df_s10['KPI1'] / q1) * q2
                #previsao de hc (media * n)
                df_s10['KPI3'] = (df_s10['KPI3'] / q1) * q2
                #previsao de inc (media * n)
                df_s10['KPI4'] = (df_s10['KPI4'] / q1) * q2
                #previsao de pl (ultimo pl + media incremento)
                df_s10['KPI8'] = df_s10['KPI8'] + (df_s10['KPI4'] / q2)
                #running fat (previsao fat / metas fat)
                df_s10['KPI10'] = df_s10['KPI1'] / df_s10['KPI2']
                #running pl (previsao pl / meta pl)
                df_s10['KPI11'] = df_s10['KPI8'] / df_s10['KPI6']

                df_s10['KPI1'] = np.where(df_s10['KPI5'] == posicao, (((df_s10['KPI1'] / q2) * q1) + faturamento), df_s10['KPI1'])
                df_s10['KPI3'] = np.where(df_s10['KPI5'] == posicao, (((df_s10['KPI3'] / q2) * q1) + saldo), df_s10['KPI3'])
                df_s10['KPI8'] = np.where(df_s10['KPI5'] == posicao, ((df_s10['KPI8'] - (df_s10['KPI4'] / q2)) + incremento), df_s10['KPI8'])
                df_s10['KPI4'] = np.where(df_s10['KPI5'] == posicao, (((df_s10['KPI4'] / q2) * q1) + incremento), df_s10['KPI4'])
                df_s10['KPI10'] = np.where(df_s10['KPI5'] == posicao, (df_s10['KPI1'] / df_s10['KPI2']), df_s10['KPI10'])
                df_s10['KPI11'] = np.where(df_s10['KPI5'] == posicao, (df_s10['KPI8'] / df_s10['KPI6']), df_s10['KPI11'])

                df_s10['KPI111'] = df_s10['KPI1'].rank(ascending=True)
                df_s10['KPI1010'] = df_s10['KPI10'].rank(ascending=True)
                df_s10['KPI44'] = df_s10['KPI4'].rank(ascending=True)
                df_s10['KPI1111'] = df_s10['KPI11'].rank(ascending=True)
                df_s10['KPI33'] = df_s10['KPI3'].rank(ascending=True)

                p1 = 0.15
                p10 = 0.15
                p4 = 0.2
                p11 = 0.2
                p3 = 0.3

                df_s10['KPI12'] = (p1 * df_s10['KPI111']) + (p10 * df_s10['KPI1010']) + (p3 * df_s10['KPI33']) + (p4 * df_s10['KPI44']) + (p11 * df_s10['KPI1111'])
                df_s10['KPI13'] = df_s10['KPI12'].rank(ascending=False)

                new_p = df_s10.loc[df_s10['KPI5'] == posicao]
                new_p = pd.DataFrame(new_p)
                column = new_p.columns.get_loc('KPI13')
                new_p = new_p.iloc[0,column]
                new_p = new_p.astype(int).round(0)
                if new_p <= 10:
                    if posicao > 10:
                        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Com base nos valores preenchidos e considerando que as demais equipes/filiais continuarão no mesmo ritmo, você passaria a ocupar a {new_p}ª posição, entrando no {categoria}. Parabéns!</span>", unsafe_allow_html=True)
                    if posicao <= 10:
                        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Com base nos valores preenchidos e considerando que as demais equipes/filiais continuarão no mesmo ritmo, você passaria a ocupar a {new_p}ª posição, permanecendo no {categoria}. Parabéns!</span>", unsafe_allow_html=True)
                if new_p > 10:
                    if posicao > 10:
                        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Com base nos valores preenchidos e considerando que as demais equipes/filiais continuarão no mesmo ritmo, você passaria a ocupar a {new_p}ª posição, permanecendo fora do {categoria}.</span>", unsafe_allow_html=True)
                    if posicao <= 10:
                        st.write(f"<span style='font-family: Barlow; font-size: 14px; color: black;'>Com base nos valores preenchidos e considerando que as demais equipes/filiais continuarão no mesmo ritmo, você passaria a ocupar a {new_p}ª posição, saindo do {categoria}. Cuidado!</span>", unsafe_allow_html=True)               
