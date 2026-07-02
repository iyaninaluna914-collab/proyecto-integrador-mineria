import streamlit as st

# 1. Configuración de la página oficial
st.set_page_config(page_title="Dashboard Streaming - Portada", page_icon="🎬", layout="wide")

# ==========================================
# 2. ENCABEZADO SEGURO
# ==========================================
st.title("🎬 Proyecto Integrador - Minería de Datos I")
st.subheader("Análisis Inteligente y Perfilado en Plataformas de Streaming")

st.markdown("---")

# ==========================================
# 3. DATOS DE LOS INTEGRANTES Y CURSADA
# ==========================================
col_info1, col_info2 = st.columns(2)

with col_info1:
    st.markdown("### 👥 Integrantes del Equipo")
    st.write("• **Luna, Yanina** — *Desarrollo de Pipeline ETL y Modelado PCA*")
    st.write("• **Luna, Karina** — *Análisis Exploratorio (EDA) y Documentación Técnica*")
    
with col_info2:
    st.markdown("### 🏫 Información Académica")
    st.write("• **Comisión / Turno:** Turno Mañana")
    st.write("• **Fecha de Entrega:** Julio 2026")
    st.write("• **Estado del Tablero:** Desplegado en la Nube")

st.markdown("---")

# ==========================================
# 4. RESUMEN EJECUTIVO Y OBJETIVOS
# ==========================================
st.markdown("### 📝 Resumen del Proyecto")
st.markdown("""
Este tablero analítico interactivo procesa los registros de comportamiento de nuestra base de usuarios con el objetivo 
de transformar datos brutos en conocimiento estratégico. A lo largo del menú lateral, se documenta el ciclo completo 
de ciencia de datos aplicado sobre la plataforma de streaming:

* **📄 1. Dataset:** Auditoría estructural de la base de datos limpia y diccionario técnico de variables comerciales.
* **📈 2. EDA:** Visualización estadística segmentada en análisis Univariado, Bivariado y correlaciones complejas.
* **🧬 3. PCA:** Reducción de dimensionalidad mediante aprendizaje no supervisado para detectar perfiles de consumo.
""")

st.markdown("---")

# ==========================================
# 5. ENLACES OBLIGATORIOS (GitHub)
# ==========================================
st.markdown("### 🔗 Acceso al Repositorio Oficial")
st.write("De acuerdo con los requerimientos de la cátedra, podés revisar el código de origen y las transformaciones en el siguiente enlace público:")

# Botón nativo estándar (100% seguro contra caídas)
st.link_button("📂 Ir al Repositorio de GitHub", "https://github.com/iyanaluna914-collab/proyecto-integrador-mineria")

st.markdown(" ")
st.info("💡 **Indicación:** Utilizá el panel de navegación izquierdo para explorar secuencialmente cada etapa de la defensa.")