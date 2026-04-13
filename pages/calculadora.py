import streamlit as st

st.title("🧮 Calculadora simple")

num1 = st.number_input("Número 1")
num2 = st.number_input("Número 2")

operacion = st.selectbox("Operación", [
    "Suma",
    "Resta",
    "Multiplicación",
    "División"
])

if st.button("Calcular"):

    if operacion == "Suma":
        resultado = num1 + num2

    elif operacion == "Resta":
        resultado = num1 - num2

    elif operacion == "Multiplicación":
        resultado = num1 * num2

    elif operacion == "División":
        if num2 != 0:
            resultado = num1 / num2
        else:
            st.error("No se puede dividir entre 0")
            resultado = None

    if resultado is not None:
        st.success(f"Resultado: {resultado}")