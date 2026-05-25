import streamlit as st
from src.calculadora import somar, dividir

# Configuração da página web
st.set_page_config(page_title="Minha Calculadora", page_icon="🧮")

st.title("🧮 Calculadora na Web")
st.write("Esta página está rodando o seu código Python diretamente no navegador!")

# Campos para digitar os números
num1 = st.number_input("Digite o primeiro número", value=0.0)
num2 = st.number_input("Digite o segundo número", value=0.0)

# Escolha da operação
operacao = st.selectbox("Escolha a operação", ["Somar", "Dividir"])

st.markdown("---")

# Botão que faz a mágica acontecer
if st.button("Calcular", type="primary"):
    try:
        if operacao == "Somar":
            resultado = somar(num1, num2)
            st.success(f"**Resultado:** {resultado}")
        elif operacao == "Dividir":
            resultado = dividir(num1, num2)
            st.success(f"**Resultado:** {resultado}")
    except ValueError as e:
        st.error(f"⚠️ Erro: {e}")