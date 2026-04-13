import streamlit as st
import numpy as np

st.title("pagina 1")

st.write("Prueba")

# Ejemplo simple
data = np.random.randn(100)
st.line_chart(data)

st.success("pagina nueva prueba")