import streamlit as st

# Diccionario de oraciones en español y sus traducciones en inglés
oraciones = {
    "Hola, ¿cómo estás?": "Hello, how are you?",
    "Me gusta aprender nuevos idiomas.": "I like to learn new languages.",
    "El clima es muy agradable hoy.": "The weather is very nice today.",
    "Voy al supermercado a comprar frutas.": "I am going to the supermarket to buy fruits.",
    "¿Dónde está la estación de tren?": "Where is the train station?"
}

# Verificación de respuestas
st.title('Corrección de Traducciones')

# Mostrar las correcciones
for i, (oracion_es, respuesta_usuario) in enumerate(zip(oraciones.keys(), st.session_state.respuestas)):
    traduccion_correcta = oraciones[oracion_es]
    st.write(f'Oración en español: {oracion_es}')
    st.write(f'Traducción del usuario: {respuesta_usuario}')
    st.write(f'Traducción correcta: {traduccion_correcta}')
    if respuesta_usuario.lower().strip() == traduccion_correcta.lower().strip():
        st.success('¡Correcto!')
    else:
        st.error('Incorrecto, inténtalo de nuevo.')

# Botón para reiniciar la prueba
if st.button('Reiniciar prueba'):
    st.session_state.index = 0
    st.session_state.respuestas = []
    st.experimental_set_query_params(page='main')
    st.experimental_rerun()
