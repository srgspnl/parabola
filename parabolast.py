import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Visualizador de Parábola", layout="centered")

st.title("📈 Analisador de Função de Segundo Grau")
st.markdown("Ajuste os parâmetros abaixo para visualizar a parábola $f(x) = ax^2 + bx + c$.")

# Barra lateral para entradas de dados
st.sidebar.header("Parâmetros da Função")
a = st.sidebar.number_input("Valor de 'a'", value=1.0, step=0.5, format="%.2f")
b = st.sidebar.number_input("Valor de 'b'", value=0.0, step=0.5, format="%.2f")
c = st.sidebar.number_input("Valor de 'c'", value=0.0, step=0.5, format="%.2f")

# Verificação para evitar divisão por zero no cálculo do vértice
if a == 0:
    st.warning("O valor de 'a' não pode ser zero para uma função de segundo grau. Exibindo uma reta.")
    xv = 0
else:
    xv = -b / (2 * a)

# Slider para controlar a amplitude do zoom no gráfico
zoom = st.sidebar.slider("Amplitude do Eixo X", 5, 50, 10)

# Processamento de dados
x = np.linspace(xv - zoom, xv + zoom, 400)
y = a * x**2 + b * x + c

# Criação do gráfico com Matplotlib
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, label=f'f(x) = {a}x² + {b}x + {c}', color='#1f77b4', linewidth=2)

# Estilização do gráfico
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.legend()

# Exibição no Streamlit
st.pyplot(fig)

# Painel de informações matemáticas
st.subheader("📊 Análise Matemática")
col1, col2 = st.columns(2)

with col1:
    st.write(f"**Vértice da Parábola:**")
    st.latex(f"V = ({xv:.2f}, {a*xv**2 + b*xv + c:.2f})")

with col2:
    delta = b**2 - 4*a*c
    st.write(f"**Discriminante ($\Delta$):**")
    st.write(f"{delta:.2f}")

if delta >= 0 and a != 0:
    x1 = (-b + np.sqrt(delta)) / (2 * a)
    x2 = (-b - np.sqrt(delta)) / (2 * a)
    st.info(f"As raízes da função são: **{x1:.2f}** e **{x2:.2f}**")
elif a != 0:
    st.info("A função não possui raízes reais ($\Delta < 0$).")