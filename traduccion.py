import streamlit as st

# Título de la aplicación
st.title('Test de Traducción de Idiomas')

# Diccionario de oraciones en español y sus traducciones en inglés
oraciones = {
    "Hola, ¿cómo estás?": "Hello, how are you?",
    "Me gusta aprender nuevos idiomas.": "I like to learn new languages.",
    "El clima es muy agradable hoy.": "The weather is very nice today.",
    "Voy al supermercado a comprar frutas.": "I am going to the supermarket to buy fruits.",
    "¿Dónde está la estación de tren?": "Where is the train station?"
}

# Lista de oraciones en español
oraciones_es = list(oraciones.keys())

# Inicializar el estado de la sesión para almacenar las respuestas y el índice de la oración actual
if 'indice_oracion' not in st.session_state:
    st.session_state.indice_oracion = 0
if 'respuestas_usuario' not in st.session_state:
    st.session_state.respuestas_usuario = [""] * len(oraciones_es)
if 'respuestas_correctas' not in st.session_state:
    st.session_state.respuestas_correctas = 0

# Obtener la oración actual
oracion_actual = oraciones_es[st.session_state.indice_oracion]

# Mostrar la oración actual
st.write(f"Traduce la siguiente oración: {oracion_actual}")

# Entrada de usuario para la traducción
traduccion_usuario = st.text_input('Escribe la traducción en inglés', st.session_state.respuestas_usuario[st.session_state.indice_oracion])

# Botón para pasar a la siguiente oración
if st.button('Siguiente oración'):
    # Guardar la respuesta del usuario
    st.session_state.respuestas_usuario[st.session_state.indice_oracion] = traduccion_usuario
    
    # Avanzar a la siguiente oración si no es la última
    if st.session_state.indice_oracion < len(oraciones_es) - 1:
        st.session_state.indice_oracion += 1
    else:
        st.write("¡Has llegado a la última oración!")

# Botón para verificar todas las respuestas
if st.button('Verificar todas las respuestas'):
    st.session_state.respuestas_correctas = 0  # Reiniciar el contador de respuestas correctas
    st.write("Resultados de la traducción:")
    for i, oracion in enumerate(oraciones_es):
        traduccion_correcta = oraciones[oracion]
        traduccion_usuario = st.session_state.respuestas_usuario[i]
        st.write(f"Oración en español: {oracion}")
        st.write(f"Tu traducción: {traduccion_usuario}")
        st.write(f"Traducción correcta: {traduccion_correcta}")
        
        if traduccion_usuario.lower().strip() == traduccion_correcta.lower().strip():
            st.success('¡Correcto!')
            st.session_state.respuestas_correctas += 1
        else:
            st.error('Incorrecto')
        st.write("")
    
    # Calcular el porcentaje de respuestas correctas
    total_oraciones = len(oraciones_es)
    porcentaje_correctas = (st.session_state.respuestas_correctas / total_oraciones) * 100
    
    # Mostrar el porcentaje de respuestas correctas
    st.write(f"Tu porcentaje de respuestas correctas es: {porcentaje_correctas:.2f}%")

# Instrucciones adicionales o información
st.write("Escribe tu traducción en inglés y haz clic en 'Siguiente oración' para avanzar. Al finalizar, haz clic en 'Verificar todas las respuestas' para ver tus resultados.")
