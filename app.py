import streamlit as st
import pandas as pd
import numpy as np

import cv2
from PIL import Image


# Texto
st.title("Mi app de datos")           # Título grande
st.header("Sección 1")                # Encabezado
st.subheader("Subsección")            # Subencabezado
st.write("Texto normal con **negrita**") # Admite Markdown
st.markdown("- Item 1\n- Item 2")     # Markdown completo
st.code("print('hola')", language="python")

# DataFrame
df = pd.DataFrame({
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla'],
    'Población': [3300000, 1600000, 690000]
})
st.dataframe(df)             # tabla interactiva (con filtros)
st.table(df)                 # tabla estática

# Gráficos rápidos
st.line_chart(np.random.randn(50))
st.bar_chart(df.set_index('Ciudad')['Población'])

# Mapa
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [40.4, -3.7],
    columns=['lat', 'lon']
)
st.map(map_data)             # mapa centrado en Madrid



with st.sidebar:
    st.header("⚙️ Configuración")
    operacion = st.selectbox("Operación", ["Canny", "Blur"])
    umbral = st.slider("Umbral", 0, 255, 127)



with st.expander("Ver código fuente del procesamiento"):
    st.code("""
bordes = cv2.Canny(img_gris, 100, 200)
contornos, _ = cv2.findContours(...)
    """, language="python")


archivo = st.file_uploader(
    "Sube una imagen",
    type=["jpg", "jpeg", "png"]   # formatos permitidos
)


if archivo is not None:
    # Convertir el fichero subido a un array de NumPy
    img_pil = Image.open(archivo)
    img_np  = np.array(img_pil)           # array RGB
    img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    # Mostrar la imagen original
    st.image(img_np, caption="Imagen cargada", use_container_width=True)

    # Aquí ya puedes procesar img_bgr con OpenCV
    img_gris = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    st.image(img_gris, caption="Escala de grises", use_container_width=True)
else:
    st.info("Sube una imagen para comenzar.")