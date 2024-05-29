import streamlit as st

# Datos del cuestionario
preguntas = {
    "I can't understand this email?": ["Would you like some help?", "Don't you know?", "I suppose you can"],
    "Shall we go to the gym now?": ["i'm too tired", "it's very good", "Not at all"],
    "The company needs to decide ...... and for all what its position is on this point.": ["here", "once", "first", "finally"],
    "I was looking forward...... at the new restaurant, but iw was closed": ["to eat", "eating", "to eating", "to have eaten"],
    "...... tired Melissa is when she gets home from work, she always makes time to say goodnight to the children": ["no matter how", "Whatever", "however much", "although"],
    "I'm sorry - I didn't ...... to disturb you.": ["hope", "think", "mean", "suppose"],
    "I'm sorry - I didn't ...... to disturb you.": ["hope", "think", "mean", "suppose"],
    "I'm sorry - I didn't ...... to disturb you.": ["hope", "think", "mean", "suppose"],
}

respuestas_correctas = {
    "I can't understand this email?": "Would you like some help?",
    "Shall we go to the gym now?": "i'm too tired",
    "The company needs to decide ...... and for all what its position is on this point.": "once",
    "I'm sorry - I didn't ...... to disturb you." : "mean",
    "I was looking forward...... at the new restaurant, but iw was closed" : "to eating",
    "...... tired Melissa is when she gets home from work, she always makes time to say goodnight to the children" : "no matter how",
    "I'm sorry - I didn't ...... to disturb you." : "mean"
}

# Función para mostrar el cuestionario
def mostrar_cuestionario():
    st.title("Test de Ingles")
    respuestas_usuario = {}

    for pregunta, opciones in preguntas.items():
        respuesta = st.radio(pregunta, opciones)
        respuestas_usuario[pregunta] = respuesta

    if st.button("Enviar"):
        st.subheader("Tus respuestas")
        for pregunta, respuesta in respuestas_usuario.items():
            st.write(f"**{pregunta}**: {respuesta}")

# Función para mostrar las respuestas correctas
def mostrar_respuestas_correctas():
    st.title("Respuestas Correctas")
    for pregunta, respuesta_correcta in respuestas_correctas.items():
        st.write(f"**{pregunta}**: {respuesta_correcta}")

# Navegación entre páginas
st.sidebar.title("Navegación")
opcion = st.sidebar.radio("Elige una página:", ("Cuestionario", "Respuestas Correctas"))

if opcion == "Cuestionario":
    mostrar_cuestionario()
elif opcion == "Respuestas Correctas":
    mostrar_respuestas_correctas()
