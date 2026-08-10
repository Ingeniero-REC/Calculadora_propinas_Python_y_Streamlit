import streamlit as st
import pandas as pd

st.title("Calculadora de propinas")
st.write("Ingresa el precio de tu cuenta y mira cuánto pagarías con distintos porcentajes de propina.")

precio = st.number_input("Precio de la cuenta ($)", min_value=0.0, value=None, step=1.0, placeholder="Ingresa el precio")

if precio is not None:
    porcentajes = [5, 10, 15, 20, 25]

    filas = []
    for porcentaje in porcentajes:
        propina = precio * (porcentaje / 100)
        total = precio + propina
        filas.append({
            "Porcentaje %": f"{porcentaje}%",
            "Propina $": propina,
            "Total $": total
        })

    tabla = pd.DataFrame(filas)

    def resaltar_15(fila):
        if fila["Porcentaje %"] == "15%":
            return ["background-color: #6A5ACD; color: white"] * len(fila)
        return [""] * len(fila)

    estilo = tabla.style.apply(resaltar_15, axis=1)

    st.dataframe(
        estilo,
        hide_index=True,
        width="stretch",
        column_config={
            "Propina $": st.column_config.NumberColumn(format="%.2f"),
            "Total $": st.column_config.NumberColumn(format="%.2f"),
        }
    )
else:
    st.info("Ingresa un precio para ver la tabla de propinas.")