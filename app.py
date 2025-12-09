import streamlit as st

st.set_page_config(
    page_title="Sorteo familiar",
    page_icon="🎁",
    layout="centered"
)

st.title("🎁 Sorteo familiar de Navidad")
st.write("""
Introduce tu número secreto para saber a quién te ha tocado regalar.

Este sistema garantiza:
- Nadie se saca a sí mismo.
- Se evita, en la medida de lo posible, regalar dentro de la misma unidad familiar.
""")

# Diccionario: numero -> persona a la que le toca regalar
ASIGNACIONES = {
    1: "Elena",
    2: "JoseManuel",
    3: "Loli",
    4: "Abuela",
    5: "Lola",
    6: "Jorge hijo",
    7: "Abuelo",
    8: "Marta",
    9: "Rosa",
    10: "Ana madre",
    11: "Rodri",
    12: "Jorge padre",
    13: "Isabela",
    14: "Manu",
    15: "Carmen",
    16: "Ana hija",
    17: "Isa",
    18: "Pitu",
    19: "Dori",
}

st.markdown("---")

numero = st.number_input(
    "Introduce tu número (entero):",
    min_value=1,
    max_value=19,
    step=1,
    format="%d"
)

if st.button("Ver a quién te ha tocado"):
    destinatario = ASIGNACIONES.get(numero, None)
    if destinatario is None:
        st.error("Número no válido. Consulta con el organizador del sorteo.")
    else:
        st.success(f"🎁 A ti te ha tocado regalar a: **{destinatario}**")
        st.info("Guarda bien esta información y no se la enseñes a nadie 😉")
else:
    st.info("Escribe tu número y pulsa el botón para ver el resultado.")
