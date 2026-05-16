import streamlit as st
import plotly.express as px

st.set_page_config(page_title="PetMatch Dashboard", layout="wide")

st.title("🐾 PetMatch: Gestão de Impacto e Adoção")

# Sidebar para filtros
st.sidebar.header("Filtros")
ong_selecionada = st.sidebar.selectbox("Selecione a ONG", ["Todas", "ONG x ", "Abrigo y"])

# KPIs principais (Métricas)
col1, col2, col3 = st.columns(3)
col1.metric("Taxa de Assertividade", "78%", "+5%")
col2.metric("Tempo Médio de Adoção", "45 dias", "-2 dias")
col3.metric("Animais em Vulnerabilidade", "124", "-10")

# Visualização 1: Funil de Adoção
st.subheader("📊 Funil de Adoção")
dados_funil = dict(
    number=[1000, 450, 150, 80],
    stage=["Visualizações", "Interesse", "Visita", "Adoção Concluída"])
fig_funil = px.funnel(dados_funil, x='number', y='stage')
st.plotly_chart(fig_funil)

# Visualização 2: Mapa de Calor (Simulado)
st.subheader("📍 Concentração de Animais vs Adotantes")
# Em sequência seria implementado mapa de calor
