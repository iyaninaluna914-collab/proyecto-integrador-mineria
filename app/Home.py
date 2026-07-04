import streamlit as st

# 1. Configuración de la página oficial
st.set_page_config(page_title="Dashboard Streaming - Portada", page_icon="🎬", layout="wide")

# ==========================================
# 2. ENCABEZADO SEGURO
# ==========================================
st.caption("Proyecto académico - Ciencia de Datos e Inteligencia Artificial")
st.subheader("Análisis Inteligente y Perfilado en Plataformas de Streaming")
st.markdown("---")

# ==========================================
# 3. DATOS DE LOS INTEGRANTES Y CURSADA
# ==========================================
col_info1, col_info2 = st.columns(2)

with col_info1:
    st.markdown("### 👥 Integrantes del Equipo")
    st.write("• **Luna, Yanina** ")
    st.write("• **Luna, Karina**" )
with col_info2:
    st.markdown("### 🏫 Información Académica")
    st.write("• ** Turno:** Turno Mañana")
    st.write("• **Fecha de Entrega:** 06 de julio- 2026")
    st.write("• **Profesor:** Fernando Mubarqui")
    st.write("• **Estado del Tablero:** Desplegado en la Nube")

st.markdown("---")

# ==========================================
# 4. RESUMEN EJECUTIVO Y OBJETIVOS
# ==========================================
st.markdown("### 📝 Resumen del Proyecto")

st.markdown("""
Este dashboard permite analizar el comportamiento de usuarios en una plataforma de streaming.
Se aplica un flujo completo de ciencia de datos que incluye limpieza, análisis exploratorio (EDA)
y reducción de dimensionalidad mediante PCA, con el objetivo de identificar patrones de consumo.
""")

st.markdown("---")

# ==========================================
# 5. ENLACES OBLIGATORIOS (GitHub)
# ==========================================
st.markdown("### 🔗 Acceso al Repositorio Oficial")
st.write("De acuerdo con los requerimientos de la cátedra, podés revisar el código de origen y las transformaciones en el siguiente enlace público:")

# Botón nativo estándar (100% seguro contra caídas)
st.link_button("📂 Ir al Repositorio de GitHub", "https://github.com/iyaninaluna914-collab/proyecto-integrador-mineria")

st.markdown(" ")
st.info("💡 **Indicación:** Utilizá el panel de navegación izquierdo para explorar secuencialmente cada etapa de la defensa.")