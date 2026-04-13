import streamlit as st

st.title("📝 Editor de texto simple")

# Entrada de texto
texto = st.text_area("Escribe tu texto aquí")

# Opciones
st.sidebar.header("Opciones")

mayusculas = st.sidebar.checkbox("Convertir a MAYÚSCULAS")
minusculas = st.sidebar.checkbox("Convertir a minúsculas")
invertir = st.sidebar.checkbox("Invertir texto")

color = st.sidebar.selectbox("Color del texto", [
    "Negro",
    "Rojo",
    "Azul",
    "Verde"
])

# Procesar texto
resultado = texto

if mayusculas:
    resultado = resultado.upper()

if minusculas:
    resultado = resultado.lower()

if invertir:
    resultado = resultado[::-1]

# Colores
colores = {
    "Negro": "black",
    "Rojo": "red",
    "Azul": "blue",
    "Verde": "green"
}

# Mostrar resultado
st.subheader("📄 Resultado")

st.markdown(
    f"<p style='color:{colores[color]}; font-size:20px;'>{resultado}</p>",
    unsafe_allow_html=True
)

# Extras
st.subheader("📊 Información")

st.write(f"Número de caracteres: {len(texto)}")
st.write(f"Número de palabras: {len(texto.split())}")